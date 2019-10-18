import unittest
import pygame.draw
from bisect_rect import *

col = 0
view = None
domain = None

def getColor(p):
    global col
    col += 1
    return col

def palette():
    return [[x, x, x] for x in range(256)]

class test(unittest.TestCase):
    def setUp(self):
        self.surface = pygame.Surface((8,8), depth=8)
        global col
        col = 0

    def tearDown(self):
        self.surface = None

    def testOne(self):
        self.assertEqual(len(""), 0)

    def test_transform(self):
        v = Rect(0,0,8,8)
        d = Rect(-2,2,4,-4)
        self.assertEqual(transform([0, 0], v, d), [-2.0, 2.0])
        self.assertEqual(transform([8, 8], v, d), [2.0, -2.0])
        self.assertEqual(transform([4, 4], v, d), [0.0, 0.0])

    # def test_bisect_rect(self):
    #     r = pygame.Rect(0, 0, 512, 256)
    #     (a, b) = bisect_rect(r)
    #     self.assertEqual(a.left, 0)
    #     self.assertEqual(a.width, 256)
    #     self.assertEqual(b.width, 256)
    #     self.assertEqual(a.right, 256)
    #     self.assertEqual(b.left, 256)
    #     self.assertEqual(b.top, a.top)
    #     self.assertEqual(a.width, 256)
    #     self.assertEqual(a.height, 256)
    #
    #     rs = [pygame.Rect(0, 0, 8, 8)]
    #
    #     stepDrawRectStack(rs, surface, getColor)
    #     self.assertEqual(rs[0], pygame.Rect(1, 1, 3, 6))
    #     self.assertEqual(rs[1], pygame.Rect(4, 1, 3, 6))
    #
    #     stepDrawRectStack(rs, surface, getColor)
    #     self.assertEqual(rs[1], pygame.Rect(5, 2, 1, 2))
    #
    #     stepDrawRectStack(rs, surface, getColor)
    #     self.assertEqual(rs[1], pygame.Rect())

    def testBisectOneColumn(self):
        r = pygame.Rect(0, 0, 1, 4)
        a, b = bisect_rect(r)
        self.assertEqual(a, pygame.Rect(0, 0, 1, 2))
        self.assertEqual(b, pygame.Rect(0, 2, 1, 2))

    def testBisectOneRowOdd(self):
        r = pygame.Rect(0, 0, 5, 1)
        a, b = bisect_rect(r)
        self.assertEqual(a, pygame.Rect(0, 0, 2, 1))
        self.assertEqual(b, pygame.Rect(2, 0, 3, 1))


    def test_perimeter(self):
        r = pygame.Rect(2, 3, 5,3)
        p = perimeter(r)
        exp = [(2, 3), (3, 3), (4, 3), (5, 3), (6, 3)]
        exp.extend([(6, 4), (6, 5)])
        exp.extend([(5, 5), (4, 5), (3, 5), (2, 5)])
        exp.extend([(2, 4)])
        self.assertEqual(p, exp)


    def testUniformRect(self):
        rs = [pygame.Rect(0, 0, 8, 8)]
        expected = [[2]*8]*8
        print('Expected:\n', expected)
        stepDrawRectStack(rs, self.surface, lambda x: 2)
        with pygame.PixelArray(self.surface) as pa:
            print('PixelArray:\n', pa)
            self.assertEqual(pa[:], expected[:])

    # def test_stepDrawRectStack(self):
    #     rs = [pygame.Rect(0, 0, 8, 8)]
    #
    #     while len(rs) > 0 :
    #         stepDrawRectStack(rs, self.surface, getColor)
    #
    #     exp = [[1,2,3,4,5,6,7,8]]
    #     exp.append([28,29,30,31,43,44,45,9])
    #     exp.append([27,42,57,32,56,61,46,10])
    #     exp.append([26,41,58,33,55,62,47,11])
    #     exp.append([25,40,59,34,54,63,48,12])
    #     exp.append([24,39,60,35,53,64,49,13])
    #     exp.append([23,38,37,36,52,51,50,14])
    #     exp.append([22,21,20,19,18,17,16,15])
    #     print('exp:', exp)
    #
    #     with pygame.PixelArray(surface) as drawn:
    #         for a in range(8):
    #             for b in range(8):
    #                 self.assertEqual(drawn[a, b], expected[a,b])


    def test_allSame(self):
        pCol = [1] * 100
        self.assertTrue(allSame(pCol))

        pCol[-1] = 2
        self.assertFalse(allSame(pCol))

        self.assertFalse(allSame([]))


    def test_insetOne(self):
        r = pygame.Rect(10, 10, 100, 100)
        insetOne(r)
        self.assertEqual(r.left, 11)
        self.assertEqual(r.width, 98)

if __name__ == "__main__":
    unittest.main()
