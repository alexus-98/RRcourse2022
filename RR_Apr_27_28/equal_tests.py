# 1. Write a function in your preferred language which allows the user to convert the temperature in Fahrenheit degrees to Celsius degrees or Kelvins, depending on target parameter. The function should raise an error for any other temperature scale.

def convert(f, target='c'):
    if target == 'c':
        return (f - 32) / 1.8
    elif target == 'k':
        return ((f - 32) / 1.8) + 273.15
    else:
        raise Exception('wrong target')


convert(50)

# 2. Check whether 50, 70, and 90 degrees Fahrenheit are converted correctly to Celsius
import unittest

class TestDivide(unittest.TestCase):
    def test_right_convertion(self):
        self.assertEqual(convert(50), 10)
        self.assertAlmostEqual(convert(70), 21.11111111)
        self.assertAlmostEqual(convert(90), 32.22222222)


if __name__ == '__main__':
    unittest.main()




