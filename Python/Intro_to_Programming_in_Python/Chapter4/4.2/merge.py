import sys
import stdio
import stdarray

# a[lo,hi):要排序的子数组 n:子数组的长度 mid:中点 aux[]:用于合并的额外数组
def _merge(a,lo,mid,hi,aux):
    n=hi-lo
    i=lo
    j=mid
    for k in range(n):
        if i==mid:aux[k]=a[j];j+=1
        elif j==hi:aux[k]=a[i];i+=1
        elif a[j]<a[i]:aux[k]=a[j];j+=1
        else:aux[k]=a[i];i+=1
    a[lo:hi]=aux[0:n]

# a:原数组 
def _sort(a,lo,hi,aux):
    n=hi-lo
    if n<=1:return 

    mid=(hi+lo)//2
    _sort(a,lo,mid,aux)
    _sort(a,mid,hi,aux)
    _merge(a,lo,mid,hi,aux)

def sort(a):
    n=len(a)
    aux=stdarray.create1D(n)
    _sort(a,0,n,aux)