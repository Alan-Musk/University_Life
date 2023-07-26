class Link(object):
    empty = ()

    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

    def __len__(self):
        return 1 + len(self.rest)

    def __getitem__(self, i):
        if i == 0:
            return self.first
        return self.rest[i - 1]

    def __repr__(self):
        if self.rest==():
            return 'Link({})'.format(repr(self.first))
        return 'Link({}, {})'.format(repr(self.first),repr(self.rest))

def validate(lst):
    """Returns True if lst is a valid Link.

    >>> lst = Link(1, Link(2, Link(3)))
    >>> validate(lst)
    True
    >>> okay = Link(Link(1), Link(2))
    >>> validate(okay)
    True
    >>> bad = Link(1, 2)
    >>> validate(Link.empty)
    True
    """
    "*** YOUR CODE HERE ***"
    if lst is Link.empty:
        return True
    elif lst.rest is not Link.empty and type(lst.rest)!=Link:
        return False
    else:
        return validate(lst.rest)
    
def count(r, value):
    """Counts the number of times VALUE shows up in R.

    >>> r = Link(3, Link(3, Link(2, Link(3))))
    >>> count(r, 3)
    3
    >>> count(r, 2)
    1
    """
    "*** YOUR CODE HERE ***"
    if r is Link.empty:
        return 0
    elif r.first==value:
        return 1+count(r.rest,value)
    else:
        return count(r.rest,value)
    
def extend_link(s1, s2):
    """Extends s1 to include the elements of s2.

    >>> s1 = Link(1)
    >>> s2 = Link(2, Link(3))
    >>> extend_link(s1, s2)
    >>> s1
    Link(1, Link(2, Link(3)))
    >>> s1.rest is not s2
    True
    """
    "*** YOUR CODE HERE ***"
    if s2 is Link.empty:
        return 
    elif s1.rest is Link.empty:
        s1.rest=Link(s2.first)
        extend_link(s1.rest,s2.rest)
    else:
        extend_link(s1.rest,s2)

def deep_map(fn, lst):
    """Applies FN to every element in lst.

    >>> normal = Link(1, Link(2, Link(3)))
    >>> deep_map(lambda x: x*x, normal)
    >>> normal
    Link(1, Link(4, Link(9)))
    >>> nested = Link(Link(1, Link(2)), Link(3, Link(4)))
    >>> deep_map(lambda x: x*x, nested)
    >>> nested
    Link(Link(1, Link(4)), Link(9, Link(16)))
    """
    "*** YOUR CODE HERE ***"
    if lst is Link.empty:
        return 
    if isinstance(list.first,Link):
        deep_map(fn,lst.first)
    else:
        lst.first=fn(lst.first)
    deep_map(fn,lst.rest)
