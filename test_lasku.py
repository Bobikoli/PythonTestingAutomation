import unittest
import lasku

class TestLasku(unittest.TestCase):
    def test_add(self):
        result = lasku.add(5, 4)
        self.assertEqual(result, 9)
    
    def test_multiply(self):
        result = lasku.multiply(3, 4)
        self.assertEqual(result, 12)
    
    def test_power(self):
        result = lasku.power(2, 8)
        self.assertEqual(result, 256)



if __name__ == '__main__':
    unittest.main ()