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
    УНИВЕРСАЛЬНАЯ проверка - работает с любым кодированием от Telegram
    """
    try:
        # Пробуем ОБА варианта: с экранированием и без
        
        # ВАРИАНТ 1: Как было (для старых данных)
        result1 = verify_variant_1(init_data)
        if result1:
            logger.info("✅ Проверка пройдена (вариант 1 - старый формат)")
            return True
        
        # ВАРИАНТ 2: Без экранирования (новый формат)
        result2 = verify_variant_2(init_data)
        if result2:
            logger.info("✅ Проверка пройдена (вариант 2 - новый формат)")
            return True
        
        logger.error("❌ Оба варианта проверки не сработали")
        return False
        
    except Exception as e:
        logger.error(f"Error: {e}")
        return False


def verify_variant_1(init_data: str) -> bool:
    """Ваш текущий вариант (с экранированными слэшами)"""
    decoded = urllib.parse.unquote(init_data)
    params = {}
    real_hash = None
    
    for pair in decoded.split('&'):
        if '=' not in pair:
            continue
        key, value = pair.split('=', 1)
        if key == 'hash':
            real_hash = value
        else:
            params[key] = value
    
    if not real_hash:
        return False
    
    sorted_keys = sorted(params.keys())
    data_check = '\n'.join(f'{k}={params[k]}' for k in sorted_keys)
    
    secret_key = hmac.new(
        key=b"WebAppData",
        msg=settings.TELEGRAM_BOT_TOKEN.encode(),
        digestmod=hashlib.sha256
    ).digest()
    
    computed = hmac.new(secret_key, data_check.encode(), hashlib.sha256).hexdigest()
    return hmac.compare_digest(computed, real_hash)


def verify_variant_2(init_data: str) -> bool:
    """НОВЫЙ вариант (без экранирования слэшей)"""
    decoded = urllib.parse.unquote(init_data)
    params = {}
    real_hash = None
    
    for pair in decoded.split('&'):
        if '=' not in pair:
            continue
        key, value = pair.split('=', 1)
        if key == 'hash':
            real_hash = value
        elif key == 'user':
            # УБИРАЕМ экранирование!
            params[key] = value.replace('\\/', '/')
        else:
            params[key] = value
    
    if not real_hash:
        return False
    
    sorted_keys = sorted(params.keys())
    data_check = '\n'.join(f'{k}={params[k]}' for k in sorted_keys)
    
    secret_key = hmac.new(
        key=b"WebAppData",
        msg=settings.TELEGRAM_BOT_TOKEN.encode(),
        digestmod=hashlib.sha256
    ).digest()
    
    computed = hmac.new(secret_key, data_check.encode(), hashlib.sha256).hexdigest()
    return hmac.compare_digest(computed, real_hash)


def create_jwt_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )
    return encoded_jwt


def verify_jwt_token(token: str) -> Optional[dict]:
    try:
        logger.error(f'START verify TOKEN: {token}')
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        logger.error(f'START verify PAYLOAD: {payload}')
        return payload
    except InvalidTokenError:
        return None
