import unittest
from main import add  # assuming `add()` is defined in main.py

class TestMain(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == "__main__":
    unittest.main()
