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
    try:
        print("=" * 60)
        print("🔍 START VERIFICATION")
        print("=" * 60)
        
        if not init_data or not isinstance(init_data, str):
            print("❌ Invalid init_data")
            return False

        if not settings.TELEGRAM_BOT_TOKEN:
            print("❌ Invalid bot_token")
            return False

        # 1. Декодируем один раз
        decoded_once = urllib.parse.unquote(init_data)
        print(f"📥 Decoded once: {decoded_once[:200]}...")

        # 2. Разбираем параметры НА ДВЕ ЧАСТИ:
        # - Для проверки хеша: оригинальные значения из decoded_once
        # - Для получения user данных: очищенные значения
        
        # 2.1 Для хеша (оригинальные значения)
        hash_params = {}
        received_hash = None
        
        # 2.2 Для данных пользователя (очищенные значения)
        user_data = None
        
        for pair in decoded_once.split('&'):
            if '=' not in pair:
                continue

            key, value = pair.split('=', 1)

            if key == 'hash':
                received_hash = value
            elif key == 'user':
                # Сохраняем ОРИГИНАЛЬНОЕ значение для data_check_string
                hash_params[key] = value
                
                # Для извлечения данных пользователя - очищаем
                try:
                    cleaned_value = value.replace('\\/', '/')
                    user_data = json.loads(cleaned_value)
                    print(f"✅ User data extracted: id={user_data.get('id')}")
                except Exception as e:
                    print(f"❌ Failed to parse user JSON: {e}")
            else:
                hash_params[key] = value

        print(f"🔑 Received hash: {received_hash}")
        print(f"📊 Hash params keys: {list(hash_params.keys())}")
        
        if not received_hash:
            print("❌ No hash in init_data")
            return False

        # 3. Создаем data_check_string из ОРИГИНАЛЬНЫХ значений
        sorted_keys = sorted(hash_params.keys())
        data_check_parts = []
        
        for key in sorted_keys:
            data_check_parts.append(f'{key}={hash_params[key]}')
        
        data_check_string = '\n'.join(data_check_parts)
        print(f"📝 Data check string:\n{data_check_string}")

        # 4. Вычисляем secret_key
        secret_key = hmac.new(
            key=b"WebAppData",
            msg=settings.TELEGRAM_BOT_TOKEN.encode('utf-8'),
            digestmod=hashlib.sha256
        ).digest()

        print(f"🔐 Secret key (hex): {secret_key.hex()}")

        # 5. Вычисляем hash
        computed_hash = hmac.new(
            key=secret_key,
            msg=data_check_string.encode('utf-8'),
            digestmod=hashlib.sha256
        ).hexdigest()

        print(f"⚡ Computed hash: {computed_hash}")
        print(f"📨 Received hash: {received_hash}")
        print(f"✅ Match: {computed_hash == received_hash}")
        print("=" * 60)
        
        result = hmac.compare_digest(computed_hash, received_hash)
        return result
        
    except Exception as e:
        print(f"❌ Error verifying init_data: {e}")
        import traceback
        traceback.print_exc()
        return False


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
