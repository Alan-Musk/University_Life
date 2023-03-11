import sys
import stdio
import stdarray
from counter import Counter

def _merge(a,front,mid,after,temp):
    n=after-front
    i=front
    j=mid
    for k in range(n):
        if i==mid:temp[k]=a[j];j+=1
        elif j==after:temp[k]=a[i];i+=1
        elif a[i]>a[j]:temp[k]=a[j];j+=1
        else:temp[k]=a[i];i+=1
    a[front:after]=temp[0:n]

def _sort(a,front,after,temp):
    n=after-front
    if n<=1:return 

    mid=(front+after)//2
    _sort(a,front,mid,temp)
    _sort(a,mid,after,temp)
    _merge(a,front,mid,after,temp)

# a[front,after) temp:临时数组
def sortMy(a):
    n=len(a)
    temp=stdarray.create1D(n)
    _sort(a,0,n,temp)


words=stdio.readAllStrings()
sortMy(words)
zipf=[]
for i in range(len(words)):
    if(i==0)or(words[i]!=words[i-1]):
        entry=Counter(words[i],len(words))
        zipf+=[entry]
    zipf[len(zipf)-1].increment()
sortMy(zipf)
zipf.reverse()
for entry in zipf:
    stdio.writeln(entry)