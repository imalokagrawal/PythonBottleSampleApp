import unittest

class Test_test_unittest(unittest.TestCase):
    def test_Sample(self):
        self.assertEqual('test'.upper(), 'TEST')

if __name__ == '__main__':
    unittest.main()


