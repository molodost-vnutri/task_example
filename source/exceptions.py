from fastapi import HTTPException

PhoneValidationException = HTTPException(
    status_code=400,
    detail='Введён некорректный номер'
)

PutDataException = HTTPException(
    status_code=400,
    detail='Произошла ошибка при добавлении данных, проверьте валидность данных и повтороите попытку'
)

GetDataException = HTTPException(
    status_code=400,
    detail='Получены не валидные данные, проверьте правильность данных и повтроите попытку'
)

RedisException = HTTPException(
    status_code=400,
    detail='Произошла ошибка, но вы не виноваты, мы уже работаем над исправлением'
)

PhoneNotExistException = HTTPException(
    status_code=404,
    detail='Телефон не найден'
)

AddressIncorrectException = HTTPException(
    status_code=400,
    detail='Адрес указан не верно'
)