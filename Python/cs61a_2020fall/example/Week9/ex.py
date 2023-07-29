
def reverse_other(t):
    def reverse(t,bl):
        if t.is_leaf():
            return 
        new_labs=[child.label for child in t.branches][::-1]
        for i in range(len(t.branches)):
            child=t.branches[i]
            reverse(child,not bl)
            if bl:
                child.label=new_labs[i]

    
    return reverse(t,True)

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