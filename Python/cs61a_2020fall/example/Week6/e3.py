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

def contains(t,e):
    if label(t)==e:
        return True
    elif is_leaf(t):
        return False
    else:
        for b in branches(t):
            if contains(b,e):
                return True
        return False

def contains(tree,e):
    if is_leaf(tree):
        return label(tree)==e
    return any([label(tree)==e]+[contains(b,e) for b in branches(tree)])



def all_paths(t):
    if is_leaf(t):
        return [[label(t)]]
    else:
        total=[]
        for b in branches(t):
            for path in all_paths(b):
                total.append([label(t)]+path)
    return total

def max_tree(t):
    if is_leaf(t):
        return tree(label(t))
    else:
        new_subtrees=[max_tree(b) for b in branches(t)]
        new_root=max([label(t)]+[label(s) for s in new_subtrees])
        return tree(new_root,new_subtrees)

