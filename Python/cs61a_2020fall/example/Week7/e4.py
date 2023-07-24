def tree(label,branches=[]):
    return [label]+branches

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree)!=list or len(tree)<1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def equal_tree(t1,t2):
    
    if label(t1)!=label(t2):
        return False
    elif len(branches(t1))!=len(branches(t2)):
        return False
    else:
        return all(equal_tree(b1,b2) for b1,b2 in zip(branches(t1),branches(t2)))

def count_tree(t):
    if is_leaf(t):
        return 1
    return 1+sum(count_tree(b) for b in branches(t))

def high_tree(t):
    if is_leaf(t):
        return 0
    return 1+max(high_tree(b) for b in branches(t))

def same_shape(t1,t2):
    if not branches(t1) or not branches(t2):
        return not branches(t1) and not branches(t2)
    elif len(branches(t1)) !=len(branches(t2)):
        return False
    return all(same_shape(b1,b2) for b1,b2 in zip(branches(t1),branches(t2)))

def sprout_leaves(t,vals):
    if is_leaf(t):
        return tree(label(t),[vals])
    return tree(label(t),[sprout_leaves(b,vals) for b in branches(t)])

def prune_leaves(t,vals):
    if is_leaf(t):
        if label(t) in vals:
            return []
        return label(t)
    return tree(label(t),[prune_leaves(b,vals) for b in branches(t)])


t1 = tree(1,[tree(2, [tree(4)]),tree(3)])
t2 = tree(1,[tree(2, [tree(4)]),tree(3)])
print(high_tree(t1))
print(prune_leaves(t1,[1,2,3]))