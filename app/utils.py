import string


def calculate_discount(price: float, discount: float) -> float:
    try:
        new_price = round(price * (1 - discount / 100), 2)
    except:
        new_price = round(price, 2)
    return new_price

def is_even(number : int) -> bool:
    result = number % 2 == 0
    return result

def get_full_name(first_name : str, last_name : str) -> str:
    full_name = f"{first_name} {last_name}"
    return full_name

def is_password_strong(password: str) -> bool:
    if len(password) < 8:
        return False

    if not any(char in string.punctuation for char in password):
        return False

    if any(char in string.whitespace for char in password):
        return False
    
    if not any(char.isupper() for char in password) or not any(char.islower() for char in password):
        return False
    
    if not any(char.isdigit() for char in password):
        return False
    
    return True
