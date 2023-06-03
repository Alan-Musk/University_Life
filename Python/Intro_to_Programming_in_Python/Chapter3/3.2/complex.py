import math
import stdio

class Complex:
    def __init__(self,re=0,im=0) -> None:
        self._re=re
        self._im=im
    def re(self): return self._re
    def im(self): return self._im

    def __add__(self,other):
        re=self._re+other._re
        im=self._im+other._im
        return Complex(re,im)
    
    def __mul__(self,other):
        re=self._re*other._re-self._im*other._im
        im=self._re*other._im+self._im*other._re
        return Complex(re,im)
    
    def __abs__(self):
        return math.sqrt(self._re*self._re+self._im*self._im)
    
    def __str__(self):
        return str(self._re)+'+'+str(self._im)+'i'

def main():
    z0=Complex(1.0,1.0)
    z=z0
    
    z=z*z+z0
    z=z*z+z0
    stdio.writeln(z)

if __name__=='__main__':main()