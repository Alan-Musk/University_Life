def count(s,value):
    """Count the number of occurrences of value in sequence s."""
    total=0
    for elem in s:
        if elem ==value:
            total+=1
    return total

def divisors(n):
    return [1]+[x for x in range(2,n) if n %x==0]

def width(area,height):
    return area//height

def perimeter(width,height):
    return 2*width+2*height

def minimum_perimeter(area):
    heights=divisors(area)
    perimeters=[perimeter(width(area,h),h) for h in heights ]
    return min(perimeters)

def apply_to_all(map_fn,s):
    return [map_fn(x) for x in s]

def keep_if(filter_fn,s):
    return [x for x in s if filter_fn(x)]

def reduce(reduce_fn,s,initial):
    reduced=initial
    for x in s:
        reduced=reduce_fn(reduced,x)
    return reduced

def divisors_of(n):
    divides_n=lambda x:n%x==0
    return [1]+keep_if(divides_n,range(2,n))

from operator import add

def sum_of_divisors(n):
    return reduce(add,divisors_of(n),0)

def perfect(n):
    return sum_of_divisors(n)==n
# 2.3.6 Tree
def tree(root_label,branches=[]):
    for branch in branches:
        assert is_tree(branch),"分支必须是树"
    return [root_label]+list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) is not list or len(tree)<1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def fib_tree(n):
    if n==0 or n==1:
        return tree(n)
    else:
        left,right=fib_tree(n-2),fib_tree(n-1)
        fib_n=label(left)+label(right)
        return tree(fib_n,[left,right])
    
def count_leaves(tree):
    if is_leaf(tree):
        return 1
    else:
        branch_counts=[count_leaves(b) for b in branches(tree)]
        return sum(branch_counts)
    
def partition_tree(n,m):
    """返回一个分割树,将n分割为不超过m的若干正整数之和"""
    if n==0:
        return tree(True)
    elif n<0 or m==0:
        return tree(False)
    else:
        left=partition_tree(n-m,m) #至少一个m划分n的所有方式
        right=partition_tree(n,m-1) #包含使用不超过m-1的分割方式
        return tree(m,[left,right])

def print_parts(tree,partition=[]):
    if is_leaf(tree):
        if label(tree):
            print(' + '.join(partition))
    else:
        left,right=branches(tree)
        m=str(label(tree))
        print_parts(left,partition+[m])
        print_parts(right,partition)

def right_binarize(tree):
    """返回一个右分叉的二元树"""
    if is_leaf(tree):
        return tree
    if len(tree)>2:
        tree=[tree[0],tree[1:]]
    return [right_binarize(b) for b in tree]

# 2.3.7
empty='empty'
def is_link(s):
    '''s是一个链表,如果它是空的或一个(first,rest)对'''
    return s==empty or (len(s))==2 and is_link(s[1])

def link(first,rest):
    """使用first元素和rest元素构建一个链表"""
    assert is_link(rest),"rest必须是一个链表"
    return [first,rest]

def first(s):
    """返回链表S的first元素"""
    assert is_link(s),"first only applies to linked lists"
    assert s is not empty,"empty linked list has no first element"
    return s[0]

def rest(s):
    """返回链表s的rest元素"""
    assert is_link(s),"rest only applies to linked lists."
    assert s is not empty,"empty linked list has no rest."
    return s[1]

def len_link(s):
    """返回链表s的长度"""
    length=0
    while s is not empty:
        s,length=rest(s),length+1
    return length

def getitem_link(s,i):
    """返回链表s中索引值为i的元素"""
    while i>0:
        s,i=rest(s),i-1
    return first(s)

def len_link_recursive(s):
    """使用递归返回s的长度"""
    if s==empty:
        return 0
    return 1+len_link_recursive(rest(s))

def getitem_link_recursive(s,i):
    """返回链表s中索引值为i的元素"""
    if i==0:
        return first(s)
    return getitem_link_recursive(rest(s),i-1)

def extend_link(s,t):
    """将t插入到链表s的最后一个元素"""
    assert is_link(s) and is_link(t)
    if s==empty:
        return t
    else:
        return link(first(s),extend_link(rest(s),t))
    

def apply_to_all_link(f,s):
    """应用f到s的每个元素"""
    assert is_link(s)
    if s==empty:
        return s
    else:
        return link(f(first(s)),apply_to_all_link(f,rest(s)))

def keep_if_link(f,s):
    """返回s中f(e)为True的元素"""
    assert is_link(s)
    if s==empty:
        return s
    else:
        kept=keep_if_link(f,rest(s))
        if f(first(s)):
            return link(first(s),kept)
        else:
            return kept

def join_link(s,separator):
    """返回由分隔符分隔的s中所有元素组成的字符串"""
    if s==empty:
        return ""
    elif rest(s)==empty:
        return str(first(s))
    else:
        return str(first(s))+separator+join_link(rest(s),separator)

def partitions(n,m):
    """返回一个由n个分区组成的链表,每个分区的部分数最多为m,每个分区表示为一个链表"""
    if n==0:
        return link(empty,empty)
    elif n<0 or m==0:
        return empty
    else:
        using_m=partition_tree(n-m,m)
        with_m=apply_to_all_link(lambda s:link(m,s),using_m)
        without_m=partitions(n,m-1)
        return extend_link(with_m,without_m)