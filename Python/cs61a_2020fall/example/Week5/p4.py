def reverse(L):
    """Reverses L in place(i.e. doesn't creat new lists)."""
    for i in range(len(L)//2):
        L[i],L[-i-1]=L[-i-1],L[i]

def map_mut(f, L):
    """Mutatively maps f onto each element in L.

    >>> L = [1, 2, 3, 4]
    >>> map_mut(lambda x: x**2, L)
    >>> L
    [1, 4, 9, 16]
    """
    "*** YOUR CODE HERE ***"
    for i in range(len(L)):
        L[i]=f(L[i])
    for i in L:
        i=f(i)