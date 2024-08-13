from os import getenv

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    '''
    Получаем значения из окружения
    '''
    redis_url: str = getenv('redis_url')
    redis_port: int = getenv('redis_port')
    redis_password: str = getenv('redis_password')
settings = Settings()