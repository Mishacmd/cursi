import utils


def test_calculate_discount_1():
    assert utils.calculate_discount(100, 10) == 90.00

    
def test_calculate_discount_2():
    assert utils.calculate_discount(200, 25) == 150.00

def test_calculate_discount_3():
    assert utils.calculate_discount(50, 0) == 50.00

def test_calculate_discount_4():
    assert utils.calculate_discount(100, 100) == 0.00

def test_calculate_discount_5():
    assert utils.calculate_discount(0, 50) == 0.00
    
def test_is_even_1():
    assert utils.is_even(2) == True

def test_is_even_2():
    assert utils.is_even(3) == False

def test_is_even_3():
    assert utils.is_even(0) == True

def test_is_even_4():
    assert utils.is_even(-1) == False

def test_is_even_5():
    assert utils.is_even(-2) == True

def test_get_full_name_1():
    assert utils.get_full_name("John", "Doe") == "John Doe"

def test_get_full_name_2():
    assert utils.get_full_name("Jane", "Smith") == "Jane Smith"

def test_get_full_name_3():
    assert utils.get_full_name("Bob", "Johnson") == "Bob Johnson"

def test_get_full_name_4():
    assert utils.get_full_name("Alice", "Williams") == "Alice Williams"

def test_get_full_name_5():
    assert utils.get_full_name("Charlie", "Brown") == "Charlie Brown"