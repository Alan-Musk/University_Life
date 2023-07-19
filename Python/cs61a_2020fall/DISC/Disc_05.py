def tree(label, branches=[]):
    return [label]+branches


def label(tree):
    return tree[0]


def branches(tree):
    return tree[1:]


def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def is_leaf(tree):
    return not branches(tree)


def print_tree(tree, indent=0):
    print("    "*indent+str(label(tree)))
    for b in branches(tree):
        print_tree(b, indent+1)


def height(t):
    if is_leaf(t):
        return 0
    return 1+max([height(branch) for branch in branches(t)])


def max_path_sum(t):
    if is_leaf(t):
        return label(t)
    return label(t)+max([max_path_sum(branch) for branch in branches(t)])


def square_tree(t):
    new_tree=[]
    if is_leaf(t):
        return tree(label(t)**2,[])
    else:
        square_result = label(t)**2
        new_tree += [square_tree(b) for b in branches(t)]
    return tree(square_result, new_tree)

def find_path(tree,x):
    if label(tree)==x:
        return [label(tree)]
    for b in branches(tree):
        path=find_path(b,x)
        if path:
            return [label(tree)]+path

def prune_binary(t,nums):
    if is_leaf(t):
        if label(t) in nums:
            return t
        return None
    else:
        next_valid_nums=[n[1:] for n in nums if n[0]==label(t)]
        new_branches=[]
        for b in branches(t):
            pruned_branch=prune_binary(b,next_valid_nums)
            if prune_binary is not None:
                new_branches=new_branches+[pruned_branch]
        if not new_branches:
            return None
        return tree(label(t),new_branches)
