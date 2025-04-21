import math
import numpy as np

class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __sub__(self, no):
        return Points(self.x - no.x, self.y - no.y, self.z - no.z)
    def dot(self, no):
        return self.x * no.x + self.y * no.y + self.z * no.z
    def cross(self, no):
        vector = np.array([self.x, self.y, self.z])
        vector2 = np.array([no.x, no.y, no.z])
        wynik = np.cross(vector, vector2)
        return Points(wynik[0], wynik[1], wynik[2])
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)



input_line = input("Enter the coordinates (x1 y1 z1 x2 y2 z2 x3 y3 z3 x4 y4 z4): ")
coordinates = list(map(float, input_line.split()))

# Create Point objects
A = Points(coordinates[0], coordinates[1], coordinates[2])
B = Points(coordinates[3], coordinates[4], coordinates[5])
C = Points(coordinates[6], coordinates[7], coordinates[8])
D = Points(coordinates[9], coordinates[10], coordinates[11])

# A = Points(0, 4, 5)
# B = Points(1, 7, 6)
# C = Points(0, 5, 9)
# D = Points(1, 7, 2)

AB = A - B
BC = B - C
CD = C - D

X = AB.cross(BC)
Y = BC.cross(CD)

dot_product = X.dot(Y)
drugaczesc = X.absolute() * Y.absolute()

angle_radians = math.acos(dot_product / drugaczesc)
angle_degrees = math.degrees(angle_radians)
print("{:.2f}".format(angle_degrees))

# zadanie ze strony hackathon
