from task1 import HashTable
import unittest


class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.H = HashTable(5)

    def test_insert_and_get(self):
        self.H.insert("apple", 10)
        self.assertEqual(self.H.get("apple"), 10)
        self.assertEqual(self.H.get_size(), 1)

    def test_insert_multiple_and_get(self):
        self.H.insert("apple", 10)
        self.H.insert("orange", 20)
        self.H.insert("banana", 30)
        self.assertEqual(self.H.get("apple"), 10)
        self.assertEqual(self.H.get("orange"), 20)
        self.assertEqual(self.H.get("banana"), 30)
        self.assertEqual(self.H.get_size(), 3)

    def test_delete(self):
        self.H.insert("apple", 10)
        self.H.insert("orange", 20)
        self.H.insert("banana", 30)
        self.assertEqual(self.H.delete("apple"), 10)
        self.assertIsNone(self.H.get("apple"))
        self.assertIsNone(self.H.delete("peach"))
        self.assertEqual(self.H.get_size(), 2)


if __name__ == '__main__':
    unittest.main()
