from codecalc import calc
import pytest

#basic unittest using pytest
def test_square():
    assert calc.square(4) == 16
    
#parameter based testing
@pytest.mark.parametrize("a,b,expected", [(1,2,3), (4,5,9)])
def test_add(a,b,expected):
    assert a+b==expected
    
#test case using fixture
@pytest.fixture
def initial_list():
    return [1,2,3]

def test_length(initial_list):
       assert len(initial_list) == 3
       
#chcek exception is correctly raised or not
def test_divide():
    with pytest.raises(ZeroDivisionError):
        calc.divide(10,0)
        
#integration testing between two components
#this components can be class,module,function
def test_generate_invoice():
    final = calc.total_with_tax(100)
    assert calc.generate_bill("Chetna", final) == "Chetna owes Rs.105.0"
    
#boundary test
def test_boundary():
    assert calc.valid_age(18)
    assert calc.valid_age(60)
    assert not calc.valid_age(17)
    
#Regression test
@pytest.mark.regression #write annotation of regression
def test_negative_amount_prevention():
    def deposit(amount):
        if amount<0:
            raise ValueError("Negative not allowed")
        return amount
    with pytest.raises(ValueError):
        deposit(-500)
        
#object state driven testing
def test_device_toggle():
    #object create for device class
    d = calc.Device()
    d.toggle()
    assert d.status=="on"
    d.toggle()
    assert d.status=="off"
    
#shape and data validation testcase
def test_matrix_shape():
    mat=calc.create_matrix()
    assert mat.shape == (3,3)
    
#time based testing
import time

def test_fast_enough():
    t0=time.time()
    calc.simulate()
    assert time.time() - t0 < 1.0 #seconds