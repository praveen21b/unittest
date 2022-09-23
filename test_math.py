from math_func import add, multiply

def test_add():
    assert add(10,12) == 22
    assert add(10)

def test_add_string():
    assert add('Hello ','World') == 'Hello World'