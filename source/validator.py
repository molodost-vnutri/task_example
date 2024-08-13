from source.exceptions import PhoneValidationException

def validator_phone(phone: str):
    if phone.startswith('0'):
        raise PhoneValidationException
    if len(phone) not in range(11, 16):
        raise PhoneValidationException
    return phone