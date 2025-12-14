# security.py с PyJWT
import hashlib
import jwt  # PyJWT
from jwt.exceptions import InvalidTokenError
from datetime import datetime, timedelta
from typing import Optional
import logging
import hmac
from app.core.config import settings
import urllib

logger = logging.getLogger(__name__)


def verify_tg_init_data(init_data: str) -> bool:
    """
    Проверяет валидность Telegram WebApp initData
    
    Args:
        init_data: Строка в формате "key1=value1&key2=value2&hash=..."
    
    Returns:
        bool: True если подпись верна, False если нет
    """
    try:
        # 1. Проверка входных данных
        if not init_data or not isinstance(init_data, str):
            logger.error(f'Invalid init_data: {init_data}')
            return False

        if not settings.TELEGRAM_BOT_TOKEN:
            logger.error('Invalid bot_token')
            return False
        
        # 2. Декодируем URL-encoded строку
        decoded_data = urllib.parse.unquote(init_data)
        logger.error(f'Decoded init_data: {decoded_data}')
        
        # 3. Разбираем параметры
        pars = decoded_data.split('&')
        data_dict = {}
        hash_value = None

        for pair in pars:
            if '=' not in pair:
                continue
                
            key, value = pair.split('=', 1)  # split только по первому '='
            
            if key == 'hash':
                hash_value = value
            else:
                data_dict[key] = value
        
        logger.error(f'Hash from data: {hash_value}')
        logger.error(f'Data dict keys: {list(data_dict.keys())}')
        
        if not hash_value:
            logger.error('No hash in init_data')
            return False
        
        # 4. Создаем data_check_string
        # Нужно сортировать ключи в алфавитном порядке
        sorted_keys = sorted(data_dict.keys())
        data_check_parts = []
        
        for key in sorted_keys:
            value = data_dict[key]
            data_check_parts.append(f'{key}={value}')
        
        data_check_string = '\n'.join(data_check_parts)
        logger.error(f'Data check string:\n{data_check_string}')
        
        # 5. Вычисляем секретный ключ (ВАЖНО: правильный порядок!)
        # По документации Telegram: HMAC-SHA256 signature of the bot's token 
        # with the constant string "WebAppData" used as a key.
        secret_key = hmac.new(
            key=b"WebAppData",  # КЛЮЧ - константа "WebAppData"
            msg=settings.TELEGRAM_BOT_TOKEN.encode('utf-8'),  # СООБЩЕНИЕ - bot_token
            digestmod=hashlib.sha256
        ).digest()
        
        logger.error(f'Secret key (hex): {secret_key.hex()}')
        
        # 6. Вычисляем хеш
        computed_hash = hmac.new(
            key=secret_key,  # КЛЮЧ - секретный ключ, вычисленный выше
            msg=data_check_string.encode('utf-8'),  # СООБЩЕНИЕ - data_check_string
            digestmod=hashlib.sha256
        ).hexdigest()
        
        logger.error(f'Computed hash: {computed_hash}')
        logger.error(f'Received hash: {hash_value}')
        
        # 7. Сравниваем
        result = hmac.compare_digest(computed_hash, hash_value)
        logger.info(f'Hash comparison result: {result}')
        
        return result
        
    except Exception as e:
        logger.error(f'Error verifying init_data: {e}', exc_info=True)
        return False
# def verify_tg_init_data(init_data: str) -> bool:
#     """
#     TEMPORARY: Telegram verification disabled for debugging
#     """
#     print("=" * 50)
#     print("TELEGRAM VERIFICATION FUNCTION CALLED")
#     print("TEMPORARILY RETURNING TRUE FOR DEBUGGING")
#     print("=" * 50)
#     return True  # ← Ключевая строка!


def create_jwt_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp': expire})
    
    encoded_jwt = jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )
    return encoded_jwt


def verify_jwt_token(token: str) -> Optional[dict]:
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        return payload
    except InvalidTokenError:
        return None
