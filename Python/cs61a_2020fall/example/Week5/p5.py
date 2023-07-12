def count_stair_ways(n):
    if n==0:
        return 1
    elif n<0:
        return 0
    else:
        return count_stair_ways(n-1)+count_stair_ways(n-2)

def count_t(n,k):
    if n==0:
        return 1
    elif n<0:
        return 0
    else:
        total=0
        i=1
        while i<=k:
            total+=count_t(n-i,k)
            i+=1
        return total

def count_t(n,k):
    if k==1:
        return 1
    elif n<0:
        return 1
    elif n==0:
        return 1
    print(n,k-1)
    print(n-k,k)
    return count_t(n,k-1)+count_t(n-k,k)

def even_weighted(s):
    return [x*s.index(x) for x in s if x%2==1]
        
def max_product(s):
    print(s)
    if s==[]:
        return 1
    elif len(s)==1:
        return s[0]
    else:
        return max(max_product(s[1:]),s[0]*max_product(s[2:]))




