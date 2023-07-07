def merge(n1,n2):
    if n1==0 and n2==0:
        return 
    if n1%10 >n2%10:
        return merge(n1,n2//10)*10+n2%10
    else:
        return merge(n1//10,n2)*10+n1%10


def make_func_repeater2(f, x):
    def repeat(i):
        if i == 0:
            return x
        else:
            return f(repeat(i - 1))
    return repeat

def make_func_repeater(f, x):
    def repeat(n):
        if x == 1:
            return f(n)
        else:
            return make_func_repeater(f,x-1)(f(n))
    return repeat
