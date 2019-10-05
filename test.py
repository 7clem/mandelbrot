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

    def test_perimeter(self):
        r = pygame.Rect(2, 3, 5,3)
        p = perimeter(r)
        exp = [(2, 3), (3, 3), (4, 3), (5, 3), (6, 3)]
        exp.extend([(6, 4), (6, 5)])
        exp.extend([(5, 5), (4, 5), (3, 5), (2, 5)])
        exp.extend([(2, 4)])
        self.assertEqual(p, exp)

    def test_recu(self):
        rs = [pygame.Rect(0, 0, 256, 256)]
        drawRectStack(rs)
        self.assertEqual(rs[0], pygame.Rect(0,0, 128, 256))
        self.assertEqual(rs[1], pygame.Rect(128, 0, 128, 256))
        drawRectStack(rs)
        self.assertEqual(rs[1], pygame.Rect(128, 0, 128, 128))
        self.assertEqual(rs[2], pygame.Rect(128, 128, 128, 128))


if __name__ == "__main__":
    unittest.main()
