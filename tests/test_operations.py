from src.math_operations import add,sub

def test_add():
    assert add(2,3) == 5
    assert add(-1,1) == 0
    
def test_sub():
    assert add(5,2) == 3
    assert add(4,3) == 1
    assert add(2,2) == 0
    assert add(1,2) == -1