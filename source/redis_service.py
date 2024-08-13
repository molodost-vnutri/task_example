from redis.asyncio import Redis
from redis.exceptions import DataError

from source.exceptions import (
    GetDataException,
    PutDataException,
    RedisException,
    PhoneNotExistException
)
from source.settings import settings
from source.schemes import Data

redis = Redis(
    host=settings.redis_url,
    port=settings.redis_port,
    password=settings.redis_password
              )

async def write_data_in_redis(data: Data):
    try:
        await redis.set(data.phone, data.address)
        return {
            "status": "successfull",
            "message": "Номер успешно добавлен"
        }
    except DataError:
        raise PutDataException
    except:
        raise RedisException

async def check_phone_in_redis(phone: str):
    try:
        address = await redis.get(phone)
        if not address:
            raise PhoneNotExistException
        return {
            "phone": phone,
            "address": address.decode()
        }
    except DataError:
        raise GetDataException
    except:
        raise RedisException