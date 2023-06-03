# key 要查找的关键字,a[]排好序的数组,lo最小可能得索引值,mid中点,hi最大可能的索引值
import sys
import stdio
from instream import InStream

def _search(key,a,lo,hi):
    if hi<=lo:return -1 # 没有找到
    mid=(lo+hi)//2
    if a[mid]>key:
        return _search(key,a,lo,mid)
    elif a[mid]<key:
        return _search(key,a,mid+1,hi) # 完全排除左边部分
    else:
        return mid # 找到后返回下标

def search(key,a):
    return _search(key,a,0,len(a))

def main():
    instream=InStream(sys.argv[1])
    a=instream.readAllStrings()
    while not stdio.isEmpty():
        key=stdio.readString()
        if search(key,a)<0:stdio.writeln(key)

if __name__=='__main__':main()