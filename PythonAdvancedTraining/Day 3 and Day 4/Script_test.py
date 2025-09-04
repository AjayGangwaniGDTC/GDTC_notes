from functions import age_cat
import unittest

class TestCatAge(unittest.TestCase):
    def test_child(self):
        self.assertEqual(age_cat.categorize_by_age(0), "Child")
        self.assertEqual(age_cat.categorize_by_age(9), "Child")
        
    def test_adolescent(self):
        self.assertEqual(age_cat.categorize_by_age(10), "Adolescent")
        self.assertEqual(age_cat.categorize_by_age(18), "Adolescent")
        
    def test_adult(self):
        self.assertEqual(age_cat.categorize_by_age(19), "Adult")
        self.assertEqual(age_cat.categorize_by_age(65), "Adult")
        
    def test_goldenage(self):
        self.assertEqual(age_cat.categorize_by_age(66), "Golden Age")
        self.assertEqual(age_cat.categorize_by_age(150), "Golden Age")
        
    def test_invalidage(self):
        self.assertEqual(age_cat.categorize_by_age(151), "Invalid age: 151")
        
if __name__ == "__main__":
    unittest.main()