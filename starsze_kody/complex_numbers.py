import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)

    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)

    def __mul__(self, no):
        real = self.real * no.real - self.imaginary * no.imaginary
        imaginary = self.real * no.imaginary + self.imaginary * no.real
        return Complex(real, imaginary)

    def __truediv__(self, no):
        denom = no.real**2 + no.imaginary**2
        real = (self.real * no.real + self.imaginary * no.imaginary) / denom
        imaginary = (self.imaginary * no.real - self.real * no.imaginary) / denom
        return Complex(real, imaginary)

    def __mod__(self):
        return Complex(math.sqrt(self.real**2 + self.imaginary**2), 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


# Testowanie samo w sonbie nie dziala
x = input()
y = input()
real, imaginary = map(float, x.split())
real2, imaginary2 = map(float, y.split())
C = Complex(real, imaginary)
D = Complex(real2, imaginary2)

print(C + D)
print(C - D)
print(C * D)
print(C / D)
print(C.__mod__())
print(D.__mod__())

# zadanie ze strony hackathon