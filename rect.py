import unittest
import copy

class Rect:
    def __init__(self, l, t, w, h):
        self.l, self.t, self.w, self.h = l, t, w, h

    def split(self):
        if max(self.w, self.h) <= 4:
            return None
        b = copy.copy(self)
        if self.w >= self.h:
            self.w = int(self.w / 2)
            b.w -= self.w
            b.l += self.w
        else:
            self.h = int(self.h / 2)
            b.h -= self.h
            b.t += self.h
        return b

    def inset(self, s=1):
        self.l += s
        self.t += s
        self.w -= 2*s
        self.h -= 2*s

    def corners(self):
        ri = self.l + self.w - 1
        bo = self.t + self.h - 1
        return (self.l, self.t), (ri, self.t), (ri, bo), (self.l, bo)

    def sides(self):
        c = self.corners()
        return (c[0], c[1]), (c[1], c[2]), (c[2], c[3]), (c[3], c[0])

    def peri(self):
        s = self.sides()
        r = hLinePts(s[0])
        r.extend(vLinePts(s[1]))
        r.extend(hLinePts(s[2]))
        r.extend(vLinePts(s[3]))
        return tuple(r)

    def __eq__(self, o):
        if type(self) != type(o):
            return False
        else:
            return self.l == o.l and self.t == o.t and self.w == o.w and self.h == o.h

    def __repr__(self):
        return "Rect(%d, %d, %d, %d)" % (self.l, self.t, self.w, self.h)

def sign(x):
    if x > 0: return 1
    elif x < 0: return -1
    else: return 0

def orthoDist(a, b):
    return [(abs(a[0] - b[0]), abs(b[1] - a[1]))]

def vLinePts(s):
    a, b = s
    if a[0] != b[0]: raise ValueError("Not vertical")
    # print( a[0], a[1], b[1])
    r = range(a[1], b[1], sign(b[1] - a[1]))
    print(list(r))
    return [(a[0], y) for y in r]

def hLinePts(s):
    a, b = s
    if a[1] != b[1]: raise ValueError("Not horizontal")
    r = range(a[0], b[0], sign(b[0] - a[0]))
    print(list(r))
    return [(x, a[1]) for x in r]

class testRect(unittest.TestCase):
    def testSplitH(self):
        r = Rect(0, 0, 15, 8)
        b = r.split()
        self.assertEqual(r, Rect(0, 0, 7, 8))
        self.assertEqual(b, Rect(7, 0, 8, 8))

    def testSplitV(self):
        r = Rect(0, 0, 8, 15)
        b = r.split()
        self.assertEqual(r, Rect(0, 0, 8, 7))
        self.assertEqual(b, Rect(0, 7, 8, 8))

    def testSplitSmall(self):
        r = Rect(0, 0, 3, 4)
        b = r.split()
        self.assertEqual(r, Rect(0, 0, 3, 4))
        self.assertEqual(b, None)

    def testInset(self):
        r = Rect(0, 0, 8, 15)
        r.inset()
        self.assertEqual(r, Rect(1, 1, 6, 13))

    def testcorners(self):
        r = Rect(0,0, 8,8)
        c = r.corners()
        self.assertEqual(c, ((0, 0), (7, 0), (7, 7), (0, 7)))

    def testSides(self):
        r = Rect(0, 0, 5, 8)
        s = r.sides()
        self.assertEqual(s[0], ((0, 0), (4, 0)))
        self.assertEqual(s[1], ((4, 0), (4, 7)))
        self.assertEqual(s[2], ((4, 7), (0, 7)))
        self.assertEqual(s[3], ((0, 7), (0, 0)))
        
    def testvLinePts(self):
        s = (0, 0), (0, 4)
        pts = vLinePts(s)
        self.assertEqual(pts[0], (0, 0))
        self.assertEqual(pts[3], (0, 3))
        self.assertEqual(len(pts), 4)
        try:
            hLinePts(s)
            self.fail("Should have thrown ValueError")
        except ValueError:
            pass
        except Exception:
            self.fail("Should have thrown ValueError")

    def testhLinePts(self):
        s = (0, 0), (4, 0)
        pts = hLinePts(s)
        self.assertEqual(pts[0], (0, 0))
        self.assertEqual(pts[3], (3, 0))
        self.assertEqual(len(pts), 4)
        try:
            vLinePts(s)
            self.fail("Should have thrown ValueError")
        except ValueError:
            pass
        except Exception:
            self.fail("Should have thrown ValueError")

    def testPerimeter(self):
        r = Rect(0, 0, 3, 3)
        p = r.peri()
        exp = ((0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (0, 2), (0, 1))
        self.assertEqual(p, exp)
        
if __name__ == "__main__":
    unittest.main()
