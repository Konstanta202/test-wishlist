from jose import JWTError, jwt
from datetime import datetime
from typing import Optional
import hashlib
import hmac
import logging

from app.core.config import settings


logger = logging.getLogger(__name__)


# def verify_tg_init_data(init_data: str) -> bool:
#     try:
#         logger.info(f"Verifying Telegram init data")
        
#         if not init_data or not isinstance(init_data, str):
#             logger.error(f'Invalid init_data: {init_data}')
#             return False

#         if not settings.TELEGRAM_BOT_TOKEN:
#             logger.error('TELEGRAM_BOT_TOKEN not set')
#             return False

#         logger.info(f"Parsing init data: {init_data[:100]}...")
#         pars = init_data.split('&')
#         data_dict = {}
#         hash_value = None

#         for pair in pars:
#             key, value = pair.split('=')
#             if key == 'hash':
#                 hash_value = value
#             else:
#                 data_dict[key] = value

#         if not hash_value:
#             logger.error('No hash in init data')
#             return False

#         logger.info(f"Hash from request: {hash_value}")
#         data_check = '\n'.join(
#             f'{key}={data_dict[key]}'
#             for key in sorted(data_dict.keys())
#         )

#         logger.info(f"Data check string: {data_check}")
        
#         # Преобразуем токен в bytes
#         bot_token_bytes = settings.TELEGRAM_BOT_TOKEN.encode('utf-8')
#         logger.info(f"Bot token length: {len(bot_token_bytes)} bytes")
        
#         # Создаем секретный ключ
#         secret_key = hmac.new(
#             key=bot_token_bytes,
#             msg=b"WebAppData",
#             digestmod=hashlib.sha256
#         ).digest()
        
#         logger.info(f"Secret key length: {len(secret_key)} bytes")
        
#         # Вычисляем хеш
#         computed_hash = hmac.new(
#             key=secret_key,
#             msg=data_check.encode(),
#             digestmod=hashlib.sha256
#         ).hexdigest()
        
#         logger.info(f"Computed hash: {computed_hash}")
#         logger.info(f"Expected hash: {hash_value}")
        
#         result = computed_hash == hash_value
#         logger.info(f"Verification result: {result}")
        
#         return result
        
#     except Exception as e:
#         logger.error(f'Error in verify_tg_init_data: {e}', exc_info=True)
#         return False


def verify_tg_init_data(init_data: str) -> bool:
    """
    Correct Telegram WebApp validation with debug info
    """
    try:
        print("=== DEBUG VERIFICATION ===")
        
        # 1. Покажем токен (первые несколько символов)
        token = settings.TELEGRAM_BOT_TOKEN
        print(f"Bot token exists: {bool(token)}")
        if token:
            print(f"Bot token preview: {token[:20]}...")
            print(f"Bot token length: {len(token)}")
            print(f"Bot token format (has colon): {':' in token}")
        
        # 2. Разберем параметры
        params = {}
        for pair in init_data.split('&'):
            if '=' not in pair:
                continue
            key, value = pair.split('=', 1)
            params[key] = value
            print(f"  {key}: {value[:50]}..." if len(value) > 50 else f"  {key}: {value}")
        
        hash_value = params.get('hash')
        if not hash_value:
            print("ERROR: No hash parameter")
            return False
        
        print(f"\nHash to verify: {hash_value}")
        
        # 3. Создаем data_check_string
        # Важно: исключаем только 'hash', остальные параметры включаем
        # И сортируем по алфавиту!
        check_items = []
        for key in sorted(params.keys()):
            if key != 'hash':  # исключаем только hash
                check_items.append(f"{key}={params[key]}")
        
        data_check_string = '\n'.join(check_items)
        
        print(f"\nData check string ({len(data_check_string)} chars):")
        print(data_check_string)
        print(f"Data check string bytes: {data_check_string.encode()}")
        
        # 4. Создаем secret_key
        print(f"\nCreating secret_key...")
        print(f"Key (b'WebAppData'): {b'WebAppData'}")
        print(f"Msg (bot token): {token.encode()}")
        
        secret_key = hmac.new(
            key=b"WebAppData",  # Фиксированная строка!
            msg=token.encode(),
            digestmod=hashlib.sha256
        ).digest()
        
        print(f"Secret key (hex): {secret_key.hex()}")
        print(f"Secret key length: {len(secret_key)} bytes")
        
        # 5. Вычисляем hash
        print(f"\nCalculating hash...")
        print(f"HMAC key: {secret_key.hex()[:64]}...")
        print(f"HMAC msg: {data_check_string.encode()}")
        
        calculated = hmac.new(
            key=secret_key,
            msg=data_check_string.encode(),
            digestmod=hashlib.sha256
        ).hexdigest()
        
        print(f"\nCalculated hash: {calculated}")
        print(f"Expected hash:   {hash_value}")
        print(f"Hashes match: {calculated == hash_value}")
        
        # 6. Также попробуем альтернативный вариант
        print(f"\n=== ALTERNATIVE: Try without signature ===")
        if 'signature' in params:
            # Исключаем и signature тоже
            check_items2 = []
            for key in sorted(params.keys()):
                if key not in ['hash', 'signature']:  # исключаем оба
                    check_items2.append(f"{key}={params[key]}")
            
            data_check_string2 = '\n'.join(check_items2)
            print(f"Data check string (no signature):")
            print(data_check_string2)
            
            calculated2 = hmac.new(
                key=secret_key,
                msg=data_check_string2.encode(),
                digestmod=hashlib.sha256
            ).hexdigest()
            
            print(f"Calculated (no signature): {calculated2}")
            print(f"Expected:                 {hash_value}")
            print(f"Hashes match: {calculated2 == hash_value}")
        
        # Возвращаем результат основной проверки
        return calculated == hash_value
        
    except Exception as e:
        print(f"ERROR in verification: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


def create_jwt_token(data: dict):
    to_encore = data.copy()

    expire = datetime.utcnow() + settings.ACCESS_TOKEN_EXPIRE_MINUTES

    to_encore.update({'exp': expire})

    encoder_jwt = jwt.encode(
        to_encore,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )
    return encoder_jwt


def verify_jwt_token(token: str) -> Optional[dict]:
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        return payload
    except JWTError:
        return None
