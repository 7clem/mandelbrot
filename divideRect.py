"""Functions to split pygame Rects in a recursive manner."""


from pygame import Rect


def divideRect(r):
    """Divides a rect by cutting the longest dimension in two parts."""
    if r.width * r.height <= 1:
        return
    else:
        if r.width >= r.height:
            return verticalCut(r)
        else:
            return horizontalCut(r)


def verticalCut(r):
    """Cuts a wide rect in two, side to side."""
    halfW = int(r.width / 2)
    a = Rect(r.left, r.top, halfW, r.height)
    b = Rect(r.left + halfW, r.top, r.width - halfW, r.height)
    return (a, b)


def horizontalCut(r):
    """Cuts a tall rect in two, one on top of the other."""
    halfH = int(r.height / 2)
    a = Rect(r.left, r.top, r.width, halfH)
    b = Rect(r.left, r.top + halfH, r.width, r.height - halfH)
    return (a, b)


if __name__ == "__main__":
    zones = [Rect(0, 0, 5, 3)]
    print(zones)

    while (len(zones) >= 1):
        z = divideRect(zones.pop())
        if z:
            zones.extend(z)
        print(zones)
        input("press key")
