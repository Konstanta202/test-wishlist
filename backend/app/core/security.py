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
    try:
        print("=== HASH VERIFICATION ===")
        
        # Извлекаем hash
        pairs = init_data.split('&')
        data_dict = {}
        hash_value = None
        
        for pair in pairs:
            if '=' not in pair:
                continue
            key, value = pair.split('=', 1)
            if key == 'hash':
                hash_value = value
                print(f"Hash to verify: {value}")
            else:
                data_dict[key] = value
        
        if not hash_value:
            print("No hash found")
            return False
        
        print(f"Data keys (except hash): {list(data_dict.keys())}")
        
        # Важно: Нужно исключить ТОЛЬКО 'hash', но оставить 'signature'!
        # Строка должна содержать все параметры кроме 'hash'
        check_items = []
        for key in sorted(data_dict.keys()):
            # Включаем ВСЕ ключи, включая 'signature'!
            check_items.append(f"{key}={data_dict[key]}")
        
        check_string = "\n".join(check_items)
        print(f"Check string ({len(check_string)} chars):")
        print(check_string)
        
        # Ключ для HMAC
        # Сначала создаем секретный ключ из токена бота
        secret_key = hmac.new(
            key=b"WebAppData",
            msg=settings.TELEGRAM_BOT_TOKEN.encode(),
            digestmod=hashlib.sha256
        ).digest()
        
        print(f"Secret key (first 16 bytes hex): {secret_key[:16].hex()}")
        
        # Теперь вычисляем hash
        calculated = hmac.new(
            key=secret_key,
            msg=check_string.encode(),
            digestmod=hashlib.sha256
        ).hexdigest()
        
        print(f"Calculated hash: {calculated}")
        print(f"Expected hash:   {hash_value}")
        
        result = hmac.compare_digest(calculated, hash_value)
        print(f"Verification result: {result}")
        
        return result
        
    except Exception as e:
        print(f"Error in verify_tg_init_data: {str(e)}")
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
