import unittest

from bisect_rect import *

points = []

def drawFn(p):
    points.append(p)

class test(unittest.TestCase):
    def setUp(self):
        points = []

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
        drawRectStack(rs, drawFn)
        self.assertEqual(rs[0], pygame.Rect(1, 1, 127, 254))
        self.assertEqual(rs[1], pygame.Rect(128, 1, 127, 254))
        drawRectStack(rs, drawFn)
        self.assertEqual(rs[1], pygame.Rect(129, 2, 125, 126))
        self.assertEqual(rs[2], pygame.Rect(129, 128, 125, 126))

        expectedPoints = [(x, y) for x in range (256) for y in range (255)]
        print(expectedPoints)
        pp = map(lambda p: p in expectedPoints, points)
        print(pp)
        self.assertTrue(all(pp))

    def test_allSame(self):
        pCol = [1] * 100
        self.assertTrue(allSame(pCol))

        pCol[-1] = 2
        self.assertFalse(allSame(pCol))

    def test_drawRectStack(self):
        view = pygame.Rect(0, 0, 64, 64)
        space = pygame.Rect(-2.0, -2.0, 2.0, 2.0)

    def test_insetOne(self):
        r = pygame.Rect(10, 10, 100, 100)
        insetOne(r)
        self.assertEqual(r.left, 11)
        self.assertEqual(r.width, 98)

if __name__ == "__main__":
    unittest.main()
