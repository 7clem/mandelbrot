import unittest

from bisect_rect import *

class test(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOne(self):
        self.assertEqual(len(""), 0)

    def test_bisect_rect(self):
        r = pygame.Rect(0, 0, 512, 256)
        (a, b) = bisect_rect(r)
        self.assertEqual(a.left, 0)
        self.assertEqual(a.width, 256)
        self.assertEqual(b.width, 256)
        self.assertEqual(a.right, 256)
        self.assertEqual(b.left, 256)
        self.assertEqual(b.top, a.top)
        self.assertEqual(a.width, 256)
        self.assertEqual(a.height, 256)


if __name__ == "__main__":
    unittest.main()
