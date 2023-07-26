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

def link_expression(s):
    '''Return a string that would evaluate to s.'''
    if s.rest is Link.empty:
        rest=''
    else:
        rest=', '+link_expression(s,rest)
    return 'Link({0}{1})'.format(s.first,rest)

def extend_linK(s,t):
    if s is Link.empty:
        return t
    else:
        return Link(s.first,extend_linK(s.rest,t))

def map_link(f,s):
    if s is Link.empty:
        return s
    else:
        return Link(f(s.first),map_link(s.rest))

def filter_link(f,s):
    if s is Link.empty:
        return s
    else:
        filtered=filter_link(f,s.rest)
        if f(s.first):
            return Link(s.first,filtered)

def join_link(s,separator):
    if s is Link.empty:
        return ""
    elif s.rest is Link.empty:
        return str(s.first)
    else:
        return str(s.first)+separator+join_link(s.rest,separator)
    
def partitions(n,m):
    """Return a linked list of partitions of n using parts of up to m.
    Each partition is represented as a linked list.
    """
    if n==0:
        return Link(Link.empty)
    elif n<0 or m==0:
        return Link.empty
    else:
        using_m=partitions(n-m,m)
        with_m=map_link(lambda s:Link(m,s),using_m)
        without_m=partitions(n,m-1)
        return with_m+without_m

def print_partitions(n,m):
    lists=partitions(n,m)
    strings=map_link(lambda s:join_link(s,'+'),lists)
    print(join_link(strings,'\n'))


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

# Set
def empty(s):
    return s is Link.empty

def set_contains(s,v):
    """Return True if and only if set s contains v."""
    if empty(s):
        return False
    elif s.first==v:
        return True
    else:
        return set_contains(s.rest,v)
    
def adjoin_set(s,v):
    """Return a set containing all elements of s and element v."""
    if set_contains(s,v):
        return s
    else:
        return Link(v,s)

def intersect_set(set1,set2):
    '''Return a set containing all elements common to set1 and set2'''
    return keep_if_link(set1,lambda v:set_contains(set2,v))

def union_set(set1,set2):
    '''Return a set containing all elements either in set1 or set2'''
    set1_not_set2=keep_if_link(set1,lambda v:not set_contains(set2,v))
    return extend_linK(set1_not_set2,set2)

# reload set_contains in ordered set
def set_contains(s,v):
    if empty(s) or s.first>v:
        return False
    elif s.first==v:
        return True
    else:
        return set_contains(s.rest,v)

def intersect_set(set1,set2):
    if empty(set1) or empty(set2):
        return Link.empty
    else:
        e1,e2=set1.first,set2.first
        if e1==e2:
            return Link(e1,intersect_set(set1.rest,set2.rest))
        elif e1<e2:
            return intersect_set(set1.rest,set2)
        elif e2<e1:
            return intersect_set(set1,set2.rest)

# reload set_contains again in binary
def set_contains(s,v):
    if s is None:
        return False
    elif s.entry==v:
        return True
    elif s.entry<v:
        return set_contains(s.right,v)
    elif s.entry>v:
        return set_contains(s.left,v)
    
def adjoin_set(s,v):
    if s is None:
        return Tree(v)
    elif s.entry==v:
        return s
    elif s.entry<v:
        return Tree(s.entry,s.left,adjoin_set(s.right,v))
    elif s.entry>v:
        return Tree(s.entry,adjoin_set(s.left,v),s.right)
        