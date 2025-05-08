import unittest
import xmlrunner
from stack import Stack

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack(3)

    def test_push_and_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)

    def test_peek(self):
        self.stack.push('a')
        self.assertEqual(self.stack.peek(), 'a')
        self.stack.push('b')
        self.assertEqual(self.stack.peek(), 'b')

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push(5)
        self.assertFalse(self.stack.is_empty())
        self.stack.pop()
        self.assertTrue(self.stack.is_empty())

    def test_is_full(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertTrue(self.stack.is_full())

    def test_overflow(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        with self.assertRaises(OverflowError):
            self.stack.push(4)

    def test_underflow(self):
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_peek_empty(self):
        with self.assertRaises(IndexError):
            self.stack.peek()

    def test_size(self):
        self.assertEqual(self.stack.size(), 0)
        self.stack.push(10)
        self.assertEqual(self.stack.size(), 1)
        self.stack.push(20)
        self.stack.pop()
        self.assertEqual(self.stack.size(), 1)

if __name__ == '__main__':
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
        failfast=False, buffer=False, catchbreak=False
    )
