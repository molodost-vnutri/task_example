from fastapi import APIRouter, Depends

from source.validator import validator_phone
from source.redis_service import check_phone_in_redis, write_data_in_redis
from source.schemes import Data

router = APIRouter(
    tags=['Эндпоинты']
)

@router.get('/check_data', status_code=200)
async def check_data_router(phone: str = Depends(validator_phone)) -> dict[str, str]:
    '''
    Ручка добавления номера и адреса в redis
    Example:
        {
        "phone": "79999999999",
        "address": "Москва, улица пушкина 53"
        }
    '''
    return await check_phone_in_redis(phone=phone)

@router.post('/write_data', status_code=201)
async def write_data_router(data: Data) -> dict[str, str]:
    '''
    Ручка получения данных из redis
    '''
    return await write_data_in_redis(data=data)