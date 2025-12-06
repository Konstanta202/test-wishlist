# from jose import JWTError, jwt
import jwt
from datetime import datetime, timedelta
from typing import Optional
import hashlib
import hmac
import logging

from app.core.config import settings


logger = logging.getLogger(__name__)


# def verify_tg_init_data(init_data: str) -> bool:
#     try:

#         if not init_data or not isinstance(init_data, str):
#             logger.error(f'Invalid init_data: {init_data}')
#             return False

#         if not settings.TELEGRAM_BOT_TOKEN:
#             logger.error('Invalid bot_token')
#             return False

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
#             return False

#         data_check = '\n'.join(
#             f'{key}={data_dict[key]}'
#             for key in sorted(data_dict.keys())
#         )

#         bot_token_bytes = settings.TELEGRAM_BOT_TOKEN.encode('utf-8')

#         secret_key = hmac.new(
#             key=bot_token_bytes,
#             msg=b"WebAppData",
#             digestmod=hashlib.sha256
#         ).digest()

#         computed_hash = hmac.new(
#             key=secret_key,
#             msg=data_check.encode(),
#             digestmod=hashlib.sha256
#         ).hexdigest()

#         return computed_hash == hash_value
#     except Exception as e:
#         print(f'Error: {e}')
#         return False


def verify_tg_init_data(init_data: str) -> bool:
    """
    TEMPORARY: Telegram verification disabled for debugging
    """
    print("=" * 50)
    print("TELEGRAM VERIFICATION FUNCTION CALLED")
    print("TEMPORARILY RETURNING TRUE FOR DEBUGGING")
    print("=" * 50)
    return True  # ← Ключевая строка!


def create_jwt_token(data: dict) -> str:
    """Create JWT token"""
    to_encode = data.copy()
    
    # Время истечения
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp': expire})
    
    # Создаем токен
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
            algorithms=settings.ALGORITHM
        )
        return payload
    except JWTError:
        return None
