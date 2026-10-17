import unittest
from utils import tambah, kurang

class TestMathUtils(unittest.TestCase):
    def test_tambah(self):
        self.assertEqual(tambah(2, 3), 5)

    def test_kurang(self):
        self.assertEqual(kurang(5, 2), 3)

if __name__ == '__main__':
    unittest.main()