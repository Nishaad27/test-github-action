from src.math_operations import add,sub

def test_add():
    assert add(2,3) == 5
    assert add(-1,1) == 0
    
def test_sub():
    assert sub(5,2) == 3
    assert sub(4,3) == 1
    assert sub(2,2) == 0
    assert sub(1,2) == -1
