import sys
import stdio

def exchange(a,i,j):
    a[i],a[j]=a[j],a[i]

def sort(a):
    n=len(a)
    for i in range(1,n):
        j=i
        while(j>0) and (a[j]<a[j-1]):
            exchange(a,j,j-1)
            j-=1

def main():
    a=stdio.readAllStrings()
    sort(a)
    for s in a:
        stdio.write(s+' ')
    stdio.writeln()

if __name__=='__main__':main()