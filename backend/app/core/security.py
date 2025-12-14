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

def verify_tg_init_data(init_data: str, expires_in: int = 3600) -> bool:
    """
    Проверка Telegram WebApp initData по алгоритму @tma.js/init-data-node
    
    Args:
        init_data: Строка initData из Telegram WebApp
        expires_in: Время жизни подписи в секундах (по умолчанию 1 час)
    
    Returns:
        bool: True если подпись валидна, False если нет
    """
    try:
        print("=" * 80)
        print("🔍 TELEGRAM AUTH VALIDATION (Official Algorithm)")
        print("=" * 80)
        
        # 1. Проверка входных данных
        if not init_data or not isinstance(init_data, str):
            print("❌ Invalid init_data")
            return False

        if not settings.TELEGRAM_BOT_TOKEN:
            print("❌ No bot token configured")
            return False
        
        print(f"📥 Raw init_data length: {len(init_data)} chars")
        
        # 2. Декодируем URL-encoded строку (ОДИН РАЗ!)
        decoded = unquote(init_data)
        print(f"📥 Decoded init_data (first 200 chars): {decoded[:200]}...")
        
        # 3. Парсим параметры как в официальной библиотеке
        parsed = parse_qs(decoded, strict_parsing=False)
        print(f"📊 Parsed parameters: {list(parsed.keys())}")
        
        # 4. Извлекаем hash
        if 'hash' not in parsed or not parsed['hash']:
            print("❌ No hash parameter found")
            return False
            
        received_hash = parsed['hash'][0]
        print(f"🔑 Received hash: {received_hash}")
        
        # 5. Создаем data-check-string (исключаем hash)
        data_check_items = []
        
        # Сортируем ключи в алфавитном порядке (как в JS библиотеке)
        sorted_keys = sorted([k for k in parsed.keys() if k != 'hash'])
        
        for key in sorted_keys:
            values = parsed[key]
            if not values:
                continue
                
            # Берем первое значение (как делает parse_qs)
            value = values[0]
            data_check_items.append(f"{key}={value}")
        
        data_check_string = "\n".join(data_check_items)
        print(f"📝 Data-check-string ({len(data_check_string)} chars):")
        print(data_check_string)
        print("-" * 40)
        
        # 6. Вычисляем секретный ключ (ТОЧНО как в документации Telegram)
        # HMAC-SHA256 от bot token с ключом "WebAppData"
        secret_key = hmac.new(
            key=b"WebAppData",
            msg=settings.TELEGRAM_BOT_TOKEN.encode('utf-8'),
            digestmod=hashlib.sha256
        ).digest()
        
        print(f"🔐 Secret key (hex): {secret_key.hex()}")
        print(f"🔐 Using bot token: {settings.TELEGRAM_BOT_TOKEN[:10]}...{settings.TELEGRAM_BOT_TOKEN[-10:]}")
        
        # 7. Вычисляем hash
        computed_hash = hmac.new(
            key=secret_key,
            msg=data_check_string.encode('utf-8'),
            digestmod=hashlib.sha256
        ).hexdigest()
        
        print(f"⚡ Computed hash: {computed_hash}")
        print(f"📨 Received hash: {received_hash}")
        
        # 8. Сравниваем хеши (используем compare_digest для защиты от timing attack)
        hash_match = hmac.compare_digest(computed_hash, received_hash)
        print(f"✅ Hash match: {hash_match}")
        
        if not hash_match:
            print("❌ Hash mismatch!")
            return False
        
        # 9. Проверяем auth_date если указан expires_in (как в JS библиотеке)
        if expires_in > 0 and 'auth_date' in parsed:
            try:
                auth_date = int(parsed['auth_date'][0])
                current_time = int(time.time())
                
                print(f"⏰ Auth date: {auth_date} ({time.ctime(auth_date)})")
                print(f"⏰ Current time: {current_time} ({time.ctime(current_time)})")
                print(f"⏰ Time difference: {current_time - auth_date} seconds")
                print(f"⏰ Max allowed: {expires_in} seconds")
                
                if current_time - auth_date > expires_in:
                    print(f"❌ Auth date expired! ({current_time - auth_date} > {expires_in})")
                    return False
                    
            except (ValueError, TypeError) as e:
                print(f"⚠️ Could not parse auth_date: {e}")
                # Продолжаем если не можем распарсить дату
        
        print("🎉 Telegram authentication SUCCESSFUL!")
        print("=" * 80)
        return True
        
    except Exception as e:
        print(f"❌ Validation error: {e}")
        import traceback
        traceback.print_exc()
        print("=" * 80)
        return False


def parse_telegram_init_data(init_data_str: str) -> Dict[str, Any]:
    """
    Распарсить initData и вернуть структурированные данные (аналог parse() из JS)
    """
    try:
        decoded = unquote(init_data_str)
        parsed = parse_qs(decoded, strict_parsing=False)
        
        result = {}
        
        for key, values in parsed.items():
            if not values:
                continue
                
            value = values[0]
            
            if key == 'user':
                try:
                    result[key] = json.loads(value)
                except json.JSONDecodeError:
                    result[key] = value
            elif key in ['auth_date', 'chat_instance', 'query_id']:
                try:
                    result[key] = int(value)
                except (ValueError, TypeError):
                    result[key] = value
            else:
                result[key] = value
        
        return result
        
    except Exception as e:
        logger.error(f"Error parsing initData: {e}")
        raise ValueError(f"Failed to parse initData: {str(e)}")


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
