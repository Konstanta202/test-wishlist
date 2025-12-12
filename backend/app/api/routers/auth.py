from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession
import logging

from app.core.db import get_db
from app.core.security import (
    verify_jwt_token,
    verify_tg_init_data,
    create_jwt_token
)
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import UserService
from app.models.user import User

logger = logging.getLogger(__name__)


router = APIRouter(prefix='/auth', tags=['auth'])
security = HTTPBearer()


@router.post('/telegram')
async def auth_telegram(
    auth_data: dict,
    db: AsyncSession = Depends(get_db)
):
    logger.info(f"Received auth_telegram request: {auth_data}")
    init_data = auth_data.get('initData')
    logger.error(f'THIS IS INIT DATA: {init_data}')
    if not init_data:
        logger.error("No initData in request")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Invalid init data'
        )

    telegram_user = auth_data.get('user')
    if not telegram_user:
        logger.error("No user in request")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Invalid user data'
        )

    logger.info("Verifying Telegram init data")

    if not verify_tg_init_data(init_data=init_data):
        logger.error("Telegram signature verification failed")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid Telegram signature'
        )

    telegram_id = telegram_user.get('id')
    first_name = telegram_user.get('first_name', '')
    last_name = telegram_user.get('last_name', '')
    username = telegram_user.get('username', '')
    photo_url = telegram_user.get('photo_url', '')

    logger.info(f"Looking for user with telegram_id: {telegram_id}")
    user = await UserService.get_user_by_telegram_id(db, telegram_id)

    if not user:
        logger.info(f"Creating new user for telegram_id: {telegram_id}")
        user_create = UserCreate(
            telegram_id=telegram_id,
            name=f'{first_name} {last_name}'.strip(),
            photo=photo_url
        )
        user = await UserService.create_user(db, user_create)
    else:
        logger.info(f"Found existing user for telegram_id: {telegram_id}")
        user = UserResponse.model_validate(user)

    logger.info(f"Creating JWT token for user_id: {user.id}")
    token_data = {
        'sub': str(user.id),
        'telegram_id': str(telegram_id),
        'username': username
    }

    try:
        access_token = create_jwt_token(token_data)
        logger.info(f"JWT token created successfully")
    except Exception as e:
        logger.error(f"Error creating JWT token: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Error creating token'
        )
    return {
        'success': True,
        'token': access_token,
        'token_type': 'bearer',
        'user': user
    }

@router.post('/telegram')
async def auth_telegram(
    auth_data: dict,
    db: AsyncSession = Depends(get_db)
):
    print("=" * 60)
    print("🚀 TELEGRAM AUTH ENDPOINT START")
    print("=" * 60)
    
    try:
        # 1. Получаем данные
        print(f"1. Received auth_data: {auth_data}")
        user_service = UserService(db)
        init_data = auth_data.get('initData')
        telegram_user = auth_data.get('user')
        
        print(f"2. initData exists: {bool(init_data)}")
        print(f"3. user exists: {bool(telegram_user)}")
        
        if not init_data:
            print("❌ ERROR: No initData")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Invalid init data'
            )
        
        if not telegram_user:
            print("❌ ERROR: No user data")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Invalid user data'
            )
        
        print(f"4. User data: {telegram_user}")
        
        # 2. Проверяем подпись (теперь возвращает True)
        print(f"5. Calling verify_tg_init_data...")
        if not verify_tg_init_data(init_data=init_data):
            print("❌ Telegram signature verification failed")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Invalid Telegram signature'
            )
        print("✅ Telegram verification passed")
        
        # 3. Извлекаем данные пользователя
        telegram_id = telegram_user.get('id')
        first_name = telegram_user.get('first_name', '')
        last_name = telegram_user.get('last_name', '')
        username = telegram_user.get('username', '')
        photo_url = telegram_user.get('photo_url', '')
        
        print(f"6. Extracted: telegram_id={telegram_id}, username={username}")
        
        # 4. Ищем пользователя в БД
        print(f"7. Searching user in DB with telegram_id: {telegram_id}")
        user = await user_service.get_user_by_telegram_id(telegram_id)
        
        if not user:
            print(f"8. User not found, creating new...")
            user_create = UserCreate(
                telegram_id=telegram_id,
                name=f'{first_name} {last_name}'.strip(),
                photo=photo_url
            )
            user = await user_service.create_user(user_create)
            print(f"9. UserCreate object: {user_create}")
            
        else:
            print(f"✅ 11. User found with ID: {user.id}")
            user = UserResponse.model_validate(user)
        
        # 5. Создаем JWT токен
        print(f"12. Creating JWT token...")
        token_data = {
            'sub': str(user.id),
            'telegram_id': str(telegram_id),
            'username': username
        }
        print(f"13. Token data: {token_data}")
        
        try:
            access_token = create_jwt_token(token_data)
            print(f"✅ 14. JWT token created: {access_token[:50]}...")
        except Exception as e:
            print(f"❌ ERROR creating JWT: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail='Error creating token'
            )
        
        # 6. Возвращаем ответ
        print(f"✅ 15. Returning success response")
        print("=" * 60)
        print("🏁 TELEGRAM AUTH ENDPOINT END - SUCCESS")
        print("=" * 60)
        
        return {
            'success': True,
            'token': access_token,
            'token_type': 'bearer',
            'user': user
        }
        
    except HTTPException:
        # Перебрасываем HTTPException
        print("❌ HTTPException raised")
        raise
        
    except Exception as e:
        print(f"❌ UNEXPECTED ERROR: {e}")
        import traceback
        traceback.print_exc()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Internal server error'
        )


@router.post('/refresh')
async def refresh_token(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: AsyncSession = Depends(get_db)
):
    token = credentials.credentials
    payload = verify_jwt_token(token)

    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid Token'
        )

    user_id = int(payload.get('sub'))
    user = await UserService.get_user(db, user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='User not found'
        )

    new_oken_data = {
        'sub': str(user.id),
        'telegram_id': payload.get('telegram_id'),
        'username': payload.get('username')
    }

    new_access_token = create_jwt_token(new_oken_data)

    return {
        'success': True,
        'token': new_access_token,
        'token_type': 'bearer',
    }


@router.get('/me')
async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: AsyncSession = Depends(get_db)
):
    token = credentials.credentials
    payload = verify_jwt_token(token)

    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid Token'
        )

    user_id = int(payload.get('sub'))
    user = await UserService.get_user(db, user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='User not found'
        )

    return user
