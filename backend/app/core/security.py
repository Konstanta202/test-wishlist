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
    ИСПРАВЛЕННАЯ проверка - БЕЗ signature в data_check_string!
    """
    try:
        print("=" * 80)
        print("🚀 CORRECTED TELEGRAM VERIFICATION")
        print("=" * 80)
        
        if not init_data or not isinstance(init_data, str):
            print("❌ Invalid init_data")
            return False

        if not settings.TELEGRAM_BOT_TOKEN:
            print("❌ Invalid bot_token")
            return False

        # 1. Декодируем
        decoded_data = urllib.parse.unquote(init_data)
        print(f"📥 Decoded (first 150 chars): {decoded_data[:150]}...")
        
        # 2. Разбираем параметры - ВАЖНО: исключаем signature!
        pars = decoded_data.split('&')
        data_dict = {}
        hash_value = None

        for pair in pars:
            if '=' not in pair:
                continue
                
            key, value = pair.split('=', 1)  # split только по первому '='
            
            if key == 'hash':
                hash_value = value
            elif key == 'signature':
                # ⚠️ ВАЖНО: signature НЕ включаем в data_check_string!
                print(f"⚠️ Found signature (ignored for hash): {value[:30]}...")
                continue  # Пропускаем!
            else:
                data_dict[key] = value
        
        print(f"🔑 Received hash: {hash_value}")
        print(f"📊 Data dict keys (without signature!): {list(data_dict.keys())}")
        
        if not hash_value:
            print("❌ No hash in init_data")
            return False
        
        # 3. Создаем data_check_string БЕЗ signature
        sorted_keys = sorted(data_dict.keys())
        data_check_parts = []
        
        for key in sorted_keys:
            value = data_dict[key]
            data_check_parts.append(f'{key}={value}')
        
        data_check_string = '\n'.join(data_check_parts)
        print(f"📝 Data check string (CORRECT - no signature):")
        print(data_check_string)
        print("-" * 40)
        
        # 4. Вычисляем секретный ключ
        secret_key = hmac.new(
            key=b"WebAppData",
            msg=settings.TELEGRAM_BOT_TOKEN.encode('utf-8'),
            digestmod=hashlib.sha256
        ).digest()
        
        print(f"🔐 Secret key (hex): {secret_key.hex()}")
        print(f"🔐 Using bot token (first/last): {settings.TELEGRAM_BOT_TOKEN[:10]}...{settings.TELEGRAM_BOT_TOKEN[-10:]}")
        
        # 5. Вычисляем хеш
        computed_hash = hmac.new(
            key=secret_key,
            msg=data_check_string.encode('utf-8'),
            digestmod=hashlib.sha256
        ).hexdigest()
        
        print(f"⚡ Computed hash: {computed_hash}")
        print(f"📨 Received hash: {hash_value}")
        
        # 6. Сравниваем
        result = hmac.compare_digest(computed_hash, hash_value)
        print(f"✅ Hash comparison result: {result}")
        
        if not result:
            print("❌ HASH MISMATCH!")
            print("   Проверьте что:")
            print("   1. Bot token правильный")
            print("   2. signature НЕ включен в data_check_string")
            print("   3. Параметры отсортированы правильно")
            
            # Отладочная информация
            print(f"\n🔍 DEBUG INFO:")
            print(f"   Data check string length: {len(data_check_string)}")
            print(f"   First 100 chars: {data_check_string[:100]}")
            print(f"   Last 100 chars: {data_check_string[-100:]}")
        
        print("=" * 80)
        return result
        
    except Exception as e:
        print(f"❌ Error verifying init_data: {e}")
        import traceback
        traceback.print_exc()
        return False


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
