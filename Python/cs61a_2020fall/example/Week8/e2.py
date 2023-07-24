from math import atan2,sin,cos,pi
from fractions import gcd
# Step 1
class Number:
    def __add__(self,other):
        return self.add(other)
    def __mul__(self,other):
        return self.mul(other)

# Step 2:为复数类型恰当地定义 add 和 mul
# 这个实现假定存在两个表示复数的类，分别对应他们的两种自然表示形式。
# ComplexRI 使用实部和虚部构建一个复数。
# ComplexMA 使用幅度和角度构建一个复数。
class Complex(Number):
    def add(self,other):
        return ComplexRI(self.read+other.real,self.img+other.img)
    def mul(self,other):
        magnitue=self.magnitude*other.magnitude
        return ComplexMA(magnitue,self.angle+other.angle)

# Complex 类存储了 real 和 imag 属性并在需要时计算 magnitude 和 angle 属性。
class ComplexRI(Complex):
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    @property
    def magnitude(self):
        return (self.real**2 +self.imag**2)**0.5
    @property
    def angle(self):
        return atan2(self.imag,self.real)
    def __rper(self):
        return 'ComplexRI({0:g},{1:g})'.format(self.real,self.imag)
    
class ComplexMA(Complex):
    def __init__(self,magnitude,angle):
        self.magnitude=magnitude
        self.angle=angle
    @property
    def real(self):
        return self.magnitude*cos(self.angle)
    @property
    def imag(self):
        return self.magnitude*sin(self.angle)
    def __repr__(self):
        return "ComplexMA({0:g},{1:g}*pi)".format(self.magnitude,self.angle/pi)

# Done

# 实现Rational表示分数
from fractions import gcd
class Rational(Number):
    def __init__(self,numer,denom):
        g=gcd(numer,denom)
        self.numer=numer//g
        self.denom=denom//g
    def __repr__(self):
        return 'Rational({0},{1})'.format(self.numer,self.denom)
    def add(self,other):
        nx,dx=self.numer,self.denom
        ny,dy=other.numer,other.denom
        return Rational(nx*dy+ny*dx,dx*dy)
    def mul(self,other):
        numer=self.numer*other.numer
        denom=self.denom*other.denom
        return Rational(numer,denom)
    

# 类型派发 使用isinstance or type_tag
# 实例: 复数和分数运算
def add_complex_and_rational(c,r):
    return ComplexRI(c.real+r.numer/r.denom,c.imag)

def mul_complex_and_rational(c,r):
    r_magnitude,r_angle=r.numer/r.denom,0
    if r_magnitude<0:
        r_magnitude,r_angle=-r_magnitude,pi
    return ComplexMA(c.magnitude*r_magnitude,c.angle+r_angle)

def add_rational_and_complex(r,c):
    return add_complex_and_rational(c,r)

def mul_rational_and_complex(r,c):
    return mul_complex_and_rational(c,r)

# 利用类型派发重写Number类
class Number:
    def __add__(self,other):
        if self.type_tag==other.type_tag:
            return self.add(other)
        elif (self.type_tag,other.type_tag) in self.adders:
            return self.cross_apply(other,self.adders)
    def __mul__(self,other):
        if self.type_tag==other.type_tag:
            return self.mul(other)
        elif (self.type_tag,other.type_tag) in self.multipliers:
            return self.cross_apply(other,self.multipliers)
    def cross_apply(self,other,cross_fns):
        cross_fn=cross_fns[(self.type_tag,other.type_tag)]
        return cross_fn(self,other)
    adders={("com","rat"):add_complex_and_rational,("rat","com"):add_rational_and_complex}
    multipliers={("com","rat"):mul_complex_and_rational,("rat","com"):mul_rational_and_complex}

# 强制转换
def rational_to_complex(r):
    return ComplexRI(r.numer/r.denom,0)

class Number:
    def __add__(self,other):
        x,y=self.coerce(other)
        return x.add(y)
    def __mul__(self,other):
        x,y=self.coerce(other)
        return x.mul(y)
    def coerce(self,other):
        if self.type_tag==other.type_tag:
            return self,other
        elif (self.type_tag,other.type_tag) in self.coercions:
            return (self.coerce_to(other.type_tag),other)
        elif (other.type_tag,self.type_tag) in self.coercions:
            return (self,other.coerce_to(self.type_tag))
    def coerce_to(self,other_tag):
        coercion_fn=self.coercions[(self.type_tag,other_tag)]
        return coercion_fn(self)
    coercions={('rat','com'):rational_to_complex}
