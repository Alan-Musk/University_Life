# Tree Class
class Tree:
    def __init__(self,label,branches=()):
        self.lable=label
        for branch in branches:
            assert isinstance(branch,Tree)
        self.branches=branches
    def __repr__(self):
        if self.branches:
            return 'Tree({0},{1})'.format(self.lable,repr(self.branches))
        else:
            return 'Tree({0})'.format(repr(self.lable))
    def is_leaf(self):
        return not self.branches
    
class Link:
    '''A linked list with a first element and the rest.'''
    empty=()
    def __init__(self,first,rest=empty):
        assert rest is Link.empty or isinstance(rest,Link)
        self.first=first
        self.rest=rest
    def __getitem__(self,i):
        if i==0:
            return self.first
        else:
            return self.rest[i-1]
    def __len__(self):
        return 1+len(self.rest)

def join_link(s,separator):
    if s is Link.empty:
        return ""
    elif s.rest is Link.empty:
        return str(s.first)
    else:
        return str(s.first)+separator+join_link(s.rest,separator)
def paths(x, y):
    """Return a list of ways to reach y from x by repeated
    incrementing or doubling.
    >>> paths(3, 5)
    [[3, 4, 5]]
    >>> sorted(paths(3, 6))
    [[3, 4, 5, 6], [3, 6]]
    >>> sorted(paths(3, 9))
    [[3, 4, 5, 6, 7, 8, 9], [3, 4, 8, 9], [3, 6, 7, 8, 9]]
    >>> paths(3, 3) # No calls is a valid path
    [[3]]
    """
    
    if x==y:
        return [[x]]
    elif x>y:
        return []
    else:
        a=paths(x+1,y)
        b=paths(2*x,y)
        return [[x]+subseq for subseq in a+b]

def merge(s1,s2):
    """Merges two sorted lists"""
    if len(s1)==0:
        return s2
    elif len(s2)==0:
        return s1
    elif s1[0]<s2[0]:
        return [s1[0]]+merge(s1[1:],s2)
    else:
        return [s2[0]]+merge(s1,s2[1:])

def mergesort(seq):
    if len(seq)<=1:
        return seq
    else:
        mid=len(seq)//2
        return merge(mergesort(seq[:mid]),mergesort(seq[mid:]))

def long_paths(tree, n):
    paths=[]
    if tree.is_leaf() and n<=0:
        paths.append(Link(tree.label))
    for b in tree.branches:
        for path in long_paths(b,n-1):
            paths.append(Link(tree.label),path)
    return paths
    
