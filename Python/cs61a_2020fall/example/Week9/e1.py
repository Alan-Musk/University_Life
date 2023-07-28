def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-2)+fib(n-1)

def count(f):
    def counted(n):
        counted.call_count+=1
        return f(n)
    counted.call_count=0
    return counted

def count_frames(f):
    def counted(n):
        counted.open_count+=1
        counted.max_count=max(counted.max_count,counted.open_count)
        result=f(n)
        counted.open_count-=1
        return result
    counted.open_count=0
    counted.max_count=0
    return counted

# Memoization 用字典实现 thoughts: or may be list, set can do it also
def memo(f):
    cache={}
    def memorized(n):
        if n not in cache:
            cache[n]=f(n)
        return cache[n]
    return memorized

# Orders of Growth
from math import sqrt
def count_factors(n):
    sqrt_n=sqrt(n)
    k,factors=1,0
    while k<sqrt_n:
        if n%k==0:
            factors+=2
        k+=1
    if k*k==n:
        factors+=1
        return count_factors
    
def exp(b,n):
    if n==0:
        return 1
    return b*exp(b,n-1)

def exp_iter(b,n):
    result=1
    for _ in range(n):
        result*=b
    return result

# 快速指数运算
def square(x):
    return x*x

def fast_exp(b,n):
    if n==0:
        return 1
    if n%2==0:
        return square(fast_exp(b,n//2))
    else:
        return b*fast_exp(b,n-1)

# 对于列表的 in 运算符，其时间复杂度为 Θ(n)
