def make_sassy_function(f,msg):
    '''Returns a version of f that only works every other function call'''
    sassy=True
    def fun(*agrs):
        nonlocal sassy
        sassy=not sassy
        if sassy:
            return msg
        return f(*agrs)
    return fun

def sentence_buffer():
    """Returns a function that will return entire sentences when it
    receives a string that ends in a period.

    >>> buffer = sentence_buffer()
    >>> buffer("This")
    >>> buffer("is")
    >>> buffer("Spot.")
    'This is Spot.'
    >>> buffer("See")
    >>> buffer("Spot")
    >>> buffer("run.")
    'See Spot run.'
    """
    "*** YOUR CODE HERE ***"
    s=''
    def sentence(input_string):
        nonlocal s
        s=s+input_string+' '
        if '.' in input_string:
            result,s=s,''
            return result
    return sentence

buffer = sentence_buffer()
buffer("This")
buffer("is")
print(buffer("Spot."))
buffer("See")
buffer("Spot")
print(buffer("run."))