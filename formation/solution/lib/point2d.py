from math import sqrt


class Point2D:
    __slots__ = ['x', 'y']

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __add__(self, P):
        S = Point2D(self.x, self.y)
        S.x = self.x + P.x
        S.y = self.y + P.y
        return S

    __radd__ = __add__

    def __sub__(self, P):
        R = Point2D(self.x, self.y)
        R.x = self.x - P.x
        R.y = self.y - P.y
        return R

    __rsub__ = __sub__

    def __mul__(self, num):
        return Point2D(num * self.x, num * self.y)

    __rmul__ = __mul__

    def __pow__(self, n):
        return Point2D(self.x ** n, self.y ** n)

    def __neg__(self):
        return Point2D(- self.x, - self.y)

    def __invert__(self):
        return Point2D(1. / self.x, 1. / self.y)

    def dist(self,P):
        return sqrt(pow(self.x - P.x, 2) + pow(self.y - P.y, 2))

    def middle(self, P):
        Q = Point2D(self.x, self.y)
        R = (1. / 2.) * (P + Q)
        return R

    def translation(self, tx, ty):
        return Point2D(self.x + tx, self.y + ty)

    def coord(self):
        return [self.x, self.y]

    def coord_homogen(self):
        return [self.x, self.y, 1.0]