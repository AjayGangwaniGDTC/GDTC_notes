#import module unittest it is built in python module
import unittest
from functions import fun

class testAdd(unittest.TestCase):
    def setUp(self): #set test environment object
        print("Setting Up....")
        
    def tearDown(self): #post test_method execution
        print("Cleaning Up...")
    
    def test_add_positive(self):
        self.assertEqual(fun.add(2,3), 5)
    
    def test_add_zero(self):
        self.assertEqual(fun.add(0,0), 0)
        
    def test_add_positive_negative(self):
        self.assertEqual(fun.add(3,-1), 2)
        
    def test_add_negative(self):
        self.assertEqual(fun.add(-2,-1), -3)
        
    def test_even_func(self):
        self.assertTrue(fun.even(4))
        
    def test_itemnotinlist(self):
        n=5
        l=[10,20,30]
        self.assertNotIn(n,l)
        
    def test_divide(self):
        with self.assertRaises(ZeroDivisionError):
            fun.divide(5,0)
            
    @unittest.skip("We are testing skip annotation")
    def test_placeholder(self):
        self.assertTrue(False)
        
    def test_reverse_str(self):
        self.assertEqual(fun.reverse_words("hello world"), "world hello")
        self.assertEqual(fun.reverse_words("xyz abc ..."), "... abc xyz")
    
if __name__ == "__main__":
    unittest.main() #runner
    
    
# Test Case: bundle of code/function or methods
# Test Suite: collection of test cases
# Test Fixture: setup() and teardown()
# Test runner: component executes test cases & communicate msg directly to the developer/user 