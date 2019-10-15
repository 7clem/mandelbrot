import unittest

from bisect_rect import *

surface = pygame.Surface((8,8), depth=8)
paPoints = pygame.PixelArray(surface)
col = 0
view = None
domain = None

def drawFn(p):
    points.append(p)
    # print("{0} -> {1}".format(p, col))
    image[p[0]+p[1]*8] = col
    return col


class test(unittest.TestCase):
    def setUp(self):
        points = []

    def tearDown(self):
        pass

    def testOne(self):
        self.assertEqual(len(""), 0)

    def test_transform(self):
        v = Rect(0,0,8,8)
        d = Rect(-2,2,4,4)
        # print(type(v))
        pts = [(0, 0)]
        pts.append((0, 7))
        pts.append((7, 7))
        pts.append((7, 0))
        pts.append((4, 4))
        r = [coordView2Domain(p, v, d) for p in pts]
        exp = [(-2.0, 2.0), (2.0, 2.0), (2, -2), (-2, -2), (0, 0)]
        self.assertEqual(r, exp)

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

    def test_drawRectStack(self):
        rs = [pygame.Rect(0, 0, 8, 8)]
        col = 1
        drawRectStack(rs, drawFn)
        self.assertEqual(rs[0], pygame.Rect(1, 1, 3, 6))
        self.assertEqual(rs[1], pygame.Rect(4, 1, 3, 6))
        col = 2
        drawRectStack(rs, drawFn)
        self.assertEqual(rs[1], pygame.Rect(5, 2, 1, 2))
        # self.assertEqual(rs[2], pygame.Rect(5, 2, 1, 4))

        expectedPoints = [(x, y) for x in range (8) for y in range (8)]
        # print(expectedPoints)
        pp = map(lambda p: p in expectedPoints, points)
        pp2 = map(lambda p: p in points, expectedPoints)
        print(list(zip(expectedPoints, pp2)))
        for n, char in enumerate(image):
            print(char, end='')
            if not n % 8: print('')

        self.assertTrue(all(pp))
        self.assertTrue(all(pp2))


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
