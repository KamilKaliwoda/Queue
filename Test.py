from Queue import Queue
import unittest


class MyTestCase(unittest.TestCase):
    def test_queue(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.peek(), 2)
        q.enqueue(5)
        q.enqueue(6)
        q.enqueue(7)
        q.enqueue(8)
        self.assertEqual(q.tab, [6, 7, 8, None, None, None, 2, 3, 4, 5])
        while not q.is_empty():
            q.dequeue()
        self.assertEqual(q.is_empty(), True)


if __name__ == '__main__':
    unittest.main()
