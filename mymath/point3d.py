from math import sqrt


class Point3D:
    __slots__ = ['x', 'y', 'z']

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z
    def __del__(self):
        #del P destroy (delete) a point
        class_name = self.__class__.__name__

    def __add__(self, P):
        S = Point3D(self.x, self.y, self.z)
        S.x = self.x + P.x
        S.y = self.y + P.y
        S.z = self.z + P.z
        return S

    __radd__ = __add__

    def __sub__(self, P):
        R = Point3D(self.x, self.y, self.z)
        R.x = self.x - P.x
        R.y = self.y - P.y
        R.z = self.z - P.z
        return R

    __rsub__ = __sub__

    def __mul__(self, num):
        return Point3D(num * self.x, num * self.y, num * self.z)

    __rmul__ = __mul__

    def __pow__(self, n):
        return Point3D(self.x ** n, self.y ** n, self.z ** n)

    def __neg__(self):
        return Point3D(- self.x, - self.y, - self.z)

    def __invert__(self):
        return Point3D(1. / self.x, 1. / self.y, 1. / self.z)

    def dist(self,P):
        return sqrt(pow(self.x - P.x, 2) + pow(self.y - P.y, 2) + pow(self.z - P.z, 2))

    def middle(self, P):
        Q = Point3D(self.x, self.y, self.z)
        R = (1. / 2.) * (P + Q)
        return R

    def translation(self, tx, ty, tz):
        return Point3D(self.x + tx, self.y + ty, self.z + tz)

    def coord(self):
        return [self.x, self.y, self.z]

    def coord_homogen(self):
        return [self.x, self.y, self.z, 1.0]