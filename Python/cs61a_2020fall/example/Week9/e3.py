class Link:
    empty=()
    def __init__(self,first,rest=empty):
        assert rest is Link.empty or isinstance(rest,Link)
        self.first=first
        self.rest=rest
    
    def __repr__(self):
        if self.rest:
            rest_str=','+repr(self.rest)
        else:
            rest_str=''
        return 'Link({0}{1})'.format(repr(self.first),rest_str)

    def __str__(self):
        string='<'
        while self.rest is not Link.empty:
            string+=str(self.first)+' '
            self=self.rest
        return string+str(self.first)+'>'
    
def sum_nums(link):
    """
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    if link.rest is  Link.empty:
        return link.first
    return link.first+sum_nums(link.rest)

def multiply_link(lst_of_link):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_link([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    result=1
    for ls in range(len(lst_of_link)):
        if lst_of_link[ls] is Link.empty:
            return Link.empty
        result*=lst_of_link[ls].first
        lst_of_link[ls]=lst_of_link[ls].rest
    return Link(result,multiply_link(lst_of_link))

def flip_two(link):
    def filp_help(link,need_lip):
        if link.rest is Link.empty:
            return 
        if need_lip:
            link.first,link.rest.first=link.rest.first,link.first
        link=link.rest
        return filp_help(link,not need_lip)
    return filp_help(link,True)


def filter_link(link,f):
    """
    >>> link = Link(1, Link(2, Link(3)))
    >>> g = filter_link(link, lambda x: x % 2 == 0)
    >>> next(g)
    2
    >>> next(g)
    StopIteration
    >>> list(filter_link(link, lambda x: x % 2 != 0))
    [1, 3]
    """ 
    while link is not Link.empty:
        if f(link.first):
            yield link.first
        link=link.rest

class Tree:
    def __init__(self,label,branches=[]):
        self.label=label
        for branch in branches:
            assert isinstance(branch,Tree)
        self.branches=list(branches)
    
    def __repr__(self):
        if self.branches:
            branch_str=', '+repr(self.branches)
        else:
            branch_str=''
        return 'Tree({0}{1})'.format(repr(self.label),branch_str)
    
    def __str__(self):
        return '\n'.join(self.indented())
    
    def indented(self):
        lines=[]
        for b in self.branches:
            for line in b.indented():
                lines.append('  '+line)
        return [str(self.label)]+lines

    def is_leaf(self):
        return not self.branches
    

def make_even(t):
    if t.is_leaf():
        if t.label %2 !=0:
            t.label+=1
        return 
    if t.label %2 !=0:
            t.label+=1
    for b in t.branches:
        make_even(b)
    
def find_paths(t,entry):
    paths=[]
    if t.label==entry:
        paths.append([t.label])
    for b in t.branches:
        branch_paths=[[t.label]+path for path in find_paths(b,entry)]
        paths.extend(branch_paths)
    return paths

def combine_tree(t1,t2,combiner):
    if t1.is_leaf():
        return Tree(combiner(t1.label,t2.label))
    result=combiner(t1.label,t2.label)
    return Tree(result,[combine_tree(b1,b2,combiner) for b1,b2 in zip(t1.branches,t2.branches)])

def alt_tree_map(t,map_fn):
    def map_function(t,need):
        if need:
            label=map_fn(t.label)
        else:
            label=t.label
        if t.is_leaf():
            return Tree(t.label)
        return Tree(label,[map_function(b,not need) for b in t.branches])
    return map_function(t,True)
