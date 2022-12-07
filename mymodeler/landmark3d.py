from math import cos, sin

from mymath.matrix import matrix
from mymath.point3d import Point3D


class Landmark3D:
    __slots__ = ['o', 'x', 'y', 'z']

    def __init__(self, o: Point3D, a=0.0, b=0.0, c=0.0):

        self.o = o

        self.a = a
        self.b = b
        self.c = c

    def __del__(self):
        #del P destroy (delete) a point
        class_name = self.__class__.__name__


    def move_matrix(self):
        m = matrix(4, 4)
        m.load([[cos(self.a)*sin(self.b) - sin(self.a)*cos(self.c)*sin(self.b),      -cos(self.a)*sin(self.b)-sin(self.a)*cos(self.c)*cos(self.b),      sin(self.a)*sin(self.c),    self.o.x],
                [sin(self.a)*cos(self.b) + cos(self.a)*cos(self.c)*sin(self.b),      -sin(self.a)*sin(self.b)+cos(self.a)*cos(self.c)*cos(self.b),      -cos(self.a)*sin(self.c),   self.o.y],
                [sin(self.c)*sin(self.b),                                            sin(self.c)*cos(self.b),                                           cos(self.c),                self.o.z]
                [0.0,                                                                0.0,                                                               0.0,                        1.0]
                ])
        return m