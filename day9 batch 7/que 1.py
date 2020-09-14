import unittest
import prime_number
class testPrime(unittest.TestCase):
    def test(self):
        num = 7
        result = prime_number.prime(num)
        self.assertEqual(result,True)
if __name__ == "__main__":
    unittest.main()