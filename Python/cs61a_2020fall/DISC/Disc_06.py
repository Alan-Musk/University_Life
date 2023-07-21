def memory(n):
    def f(g):
        nonlocal n
        n=g(n)
        return n
    return f

def group_by(s,fn):
    grouped={}
    for e in s:
        key=fn(e)
        if key in grouped:
            grouped[key].append(e)
        else:
            grouped[key]=[e]
    return grouped

def add_this_many(x,el,s):
    num=s.count(x)
    s.extend([el]*num)

def filter(iterable,fn):
    for elem in iterable:
        if fn(elem):
            yield elem

def merge(a,b):
    first_a,first_b=next(a),next(b)
    while True:
        if first_a==first_b:
            yield first_a
            first_a,first_b=next(a),next(b)
        elif first_a<first_b:
            yield first_a
            first_a=next(a)
        else:
            yield first_b
            first_b=next(b)
    