# app.py
def suma(a, b):
    return a + b

# test_app.py
from app import suma

def test_suma():
    assert suma(2, 3) == 5
