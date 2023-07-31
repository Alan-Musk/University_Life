class CircularBuffer:
    """Doctests:

    >>> buffer = CircularBuffer(3)
    >>> buffer.remove()
    Buffer is empty
    >>> buffer.append('a')
    >>> buffer.remove()
    'a'
    >>> buffer.remove()
    Buffer is empty
    >>> buffer.append('b')
    >>> buffer.append('c')
    >>> buffer.append('d')
    >>> buffer.append('e')
    Buffer capacity exceeded
    >>> buffer.remove()
    'b'
    >>> buffer.remove()
    'c'
    >>> buffer.remove()
    'd'
    >>> buffer.remove()
    Buffer is empty
    """
    def __init__(self, n):
        self.array = [None]*n   # list of length n
        self.n = n
        self.start = 0
        self.end = 0

    def append(self, elem):
        "*** YOUR CODE HERE ***"
        if self.end-self.start==self.n:
            print('Buffer capacity exceeded')
        else:
            self.array[self.end%self.n]=elem
            self.end+=1
            
    def remove(self):
        "*** YOUR CODE HERE ***"
        if self.start==self.end:
            print('Buffer is empty')
        else:
            result=self.array[self.start%self.n]
            self.start+=1
            return result
class Chef:
    """Doctests:

    >>> albert = Chef('quiche', ['egg', 'cheese', 'cream', 'salt'])
    >>> ramsay = Chef('steak', ['meat', 'bbq sauce', 'salt'])
    >>> ramsay.cook()
    'Not enogh ingredients!'
    >>> ramsay.serve()
    'No food to serve!'
    >>> ramsay.fetch_ingredients()     # 1 salt remaining
    "Fetched: ['meat', 'bbq sauce', 'salt']"
    >>> ramsay.cook()
    'Cooked steak!'
    >>> ramsay.serve()
    >>> Chef.finished
    ['steak']
    >>> albert.fetch_ingredients()     # 0 salt remaining
    "Fetched: ['egg', 'cheese', 'cream', 'salt']"
    >>> albert.cook()
    'Cooked quiche!'
    >>> albert.serve()
    >>> Chef.finished
    ['steak', 'quiche']
    >>> ramsay.fetch_ingredients()
    'No more salt!'
    """
    "*** YOUR CODE HERE ***"
    finished=[]
    storage={}
    def __init__(self,name,ingredients):
        self.name=name
        self.ingredients=ingredients
        self.enough_ingredients=False
        for i in ingredients:
            if i not in Chef.storage:
                Chef.storage[i]=2

    def cook(self):
        if self.enough_ingredients:
            Chef.finished+=[self.name]
            return 'Cooked {}!'.format(self.name)
        else:
            return 'Not enogh ingredients!'
        

    def fetch_ingredients(self):
        for i in self.ingredients:
            if Chef.storage[i]<1:
                return 'No more {}!'.format(i)
        for i in self.ingredients:
            Chef.storage[i]-=1
        self.enough_ingredients=True
        return "Fetched: {}".format(self.ingredients)
    
    def serve(self):
        if Chef.finished==[]:
            return 'No food to serve!'