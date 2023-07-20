# primes=[2,3,5,7]
# print(type(primes))
# iterator=iter(primes)
# print(type(iterator))

def evens(start,end):
    even=start+(start%2)
    while even<end:
        yield even
        even+=2

def countdown(k):
    if k>0:
        yield k
        yield from countdown(k-1)
    else:
        yield "Blast off"

def prefixes(s):
    if s:
        yield from prefixes(s[:-1])
        yield s

def substrings(s):
    if s:
        yield from prefixes(s)
        yield from substrings(s[1:])

class Letters(object):
    def __init__(self):
        self.current='a'
    def __next__(self):
        if self.current>'d':
            raise StopIteration
        result=self.current
        self.current=chr(ord(result)+1)
        return result
    def __iter__(self):
        return self

class Positives:
    def __init__(self):
        self.next_positive=1
    def __next__(self):
        result=self.next_positive
        self.next_positive+=1
        return result

def letters_generator():
    current='a'
    while current<='d':
        yield current
        current=chr(ord(current)+1)

def all_pairs(s):
    for item1 in s:
        for item2 in s:
            yield(item1,item2)

class LettersWithYield:
    def __init__(self,start='a',end='e'):
        self.start=start
        self.end=end
    def __iter__(self):
        next_letter=self.start
        while next_letter<self.end:
            yield next_letter
            next_letter=chr(ord(next_letter)+1)

class LetterIter:
    '''an iterator over letters of the alphabet in ASCII order.'''
    def __init__(self,start='a',end='e'):
        self.next_letter=start
        self.end=end
    def __next__(self):
        if self.next_letter==self.end:
            raise StopIteration
        letter=self.next_letter
        self.next_letter=chr(ord(letter)+1)
        return letter
    
p=Positives()
n=1
while n<10:
    print(next(p))
    n+=1