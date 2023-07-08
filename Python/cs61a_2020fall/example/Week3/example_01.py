def repeat(k):
    """When called repeatedly,print each repeated argument."""
    return detector(lambda j:False)(k)

def detector(have_seen_i_before):
    def g(i):
        if have_seen_i_before(i):
            print(i)
        return detector(lambda j:j==i or have_seen_i_before(j))
    return g

f=repeat(1)(7)(7)(3)(4)(2)(5)(1)(2)(2)