'''
For this challenge, you are given two complex numbers, and you have to print the result of their addition, subtraction, multiplication, division and modulus operations.

The real and imaginary precision part should be correct up to two decimal places.
'''

import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real=real
        self.imaginary=imaginary
        
    def __add__(self, no):
        return Complex(self.real+no.real,self.imaginary+no.imaginary)
        
    def __mul__(self, no):#a+ib,c+id
        return Complex(self.real*no.real-self.imaginary*no.imaginary,self.real*no.imaginary+self.imaginary*no.real)
        
    def __sub__(self, no):
        return Complex(self.real-no.real,self.imaginary-no.imaginary)

    def __truediv__(self, no):
        no.imaginary=-no.imaginary
        return Complex(self.__mul__(no).real/(pow(no.real,2)+pow(no.imaginary,2)),self.__mul__(no).imaginary/(pow(no.real,2)+pow(no.imaginary,2)))
        

    def mod(self):
        return Complex(math.sqrt(pow(self.real,2)+pow(self.imaginary,2)),0)

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

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y,x/y, x.mod(), y.mod()]), sep='\n')
