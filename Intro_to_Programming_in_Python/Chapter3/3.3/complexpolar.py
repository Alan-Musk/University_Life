import math
import stdio

class Complex:
    def __init__(self,re=0,im=0) -> None:
        self._r=math.hypot(im,re)
        self._theta=math.atan2(im,re)

    def re(self):return self._r*math.cos(self._theta)
    def im(self):return self._r*math.sin(self._theta)

    def __add__(self,other):
        re=self.re()+other.re()
        im=self.im()+other.im()
        return Complex(re,im)
    
    def __mul__(self,other):
        c=Complex()
        c._r=self._r*other._r
        c._theta=self._theta+other._theta
        return c
    
    def __abs__(self):return self._r

    def __str__(self):return str(self.re())+'+'+str(self.im())+'i'

def main():
    z0=Complex(1.0,1.0)
    z=z0
    z=z*z+z0
    z=z*z+z0
    stdio.writeln(z)

if __name__=='__main__':main()