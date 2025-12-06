from jose import JWTError, jwt
from datetime import datetime
from typing import Optional
import hashlib
import hmac
import logging

from app.core.config import settings


logger = logging.getLogger(__name__)


def verify_tg_init_data(init_data: str) -> bool:
    try:
        logger.info(f"Verifying Telegram init data")
        
        if not init_data or not isinstance(init_data, str):
            logger.error(f'Invalid init_data: {init_data}')
            return False

        if not settings.TELEGRAM_BOT_TOKEN:
            logger.error('TELEGRAM_BOT_TOKEN not set')
            return False

        logger.info(f"Parsing init data: {init_data[:100]}...")
        pars = init_data.split('&')
        data_dict = {}
        hash_value = None

        for pair in pars:
            key, value = pair.split('=')
            if key == 'hash':
                hash_value = value
            else:
                data_dict[key] = value

        if not hash_value:
            logger.error('No hash in init data')
            return False

        logger.info(f"Hash from request: {hash_value}")
        data_check = '\n'.join(
            f'{key}={data_dict[key]}'
            for key in sorted(data_dict.keys())
        )

        logger.info(f"Data check string: {data_check}")
        
        # Преобразуем токен в bytes
        bot_token_bytes = settings.TELEGRAM_BOT_TOKEN.encode('utf-8')
        logger.info(f"Bot token length: {len(bot_token_bytes)} bytes")
        
        # Создаем секретный ключ
        secret_key = hmac.new(
            key=bot_token_bytes,
            msg=b"WebAppData",
            digestmod=hashlib.sha256
        ).digest()
        
        logger.info(f"Secret key length: {len(secret_key)} bytes")
        
        # Вычисляем хеш
        computed_hash = hmac.new(
            key=secret_key,
            msg=data_check.encode(),
            digestmod=hashlib.sha256
        ).hexdigest()
        
        logger.info(f"Computed hash: {computed_hash}")
        logger.info(f"Expected hash: {hash_value}")
        
        result = computed_hash == hash_value
        logger.info(f"Verification result: {result}")
        
        return result
        
    except Exception as e:
        logger.error(f'Error in verify_tg_init_data: {e}', exc_info=True)
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
