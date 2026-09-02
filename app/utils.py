def calculate_discount(price : float, discount : float) -> float:
    new_price = round(price * (discount / 100), 2)
    
    return new_price

def is_even(number : int) -> bool:
    result = number % 2 == 0
    return result

def get_full_name(first_name : str, last_name : str) -> str:
    full_name = f"{first_name} {last_name}"
    return full_name