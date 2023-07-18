def make_withdraw(balance):
    """返回一个每次调用都会减少余额的withdraw函数"""
    def withdraw(amount):
        nonlocal balance  # 申明balance是非局部的
        if amount>balance:
            return "Insufficiend funds"
        balance=balance-amount
        return balance
    return withdraw

empty='empty'

def mutable_link():
    """返回一个可变链表的函数"""
    contents=empty
    def dispatch(message,value=None):
        nonlocal contents
        if message=='len':
            return len_link(contents)
        elif message=='getitem':
            return getitem_link(contents,value)
        elif message=='push_first':
            contents=link(value,contents)
        elif message=='pop_first':
            f=first(contents)
            contents=rest(contents)
            return f
        elif message=='str':
            return join_link(contents,",")
    return dispatch

def to_mutable_link(source):
    s=mutable_link()
    for element in reversed(source):
        s('push_first',element)
    return s

def link(first,rest):
    return [first,rest]

def first(s):
    return s[0]

def rest(s):
    return s[1]

def len_link(s):
    length=0
    while s!=empty:
        s,length=rest(s),length+1
    return length

def getitem_link(s,i):
    while i>0:
        s,i=rest(s),i-1
    return first(s)

def join_link(s,separator):
    if s==empty:
        return ""
    elif rest(s)==empty:
        return str(first(s))
    else:
        return str(first(s))+separator+join_link(rest(s),separator)

"""返回一个字典的函数实现"""
def dictionary():
    records=[]
    def getitem(key):
        matches=[r for r in records if r[0]==key]
        if len(matches)==1:
            key,value=matches[0]
            return value
    
    def setitem(key,value):
        nonlocal records
        # 如果 r[0]!=key 就放入non_matches中
        non_matches=[r for r in records if r[0]!=key]
        records=non_matches+[[key,value]]
    
    def dispatch(message,key=None,value=None):
        if message=='getitem':
            return getitem(key)
        elif message=='setitem':
            setitem(key,value)
    return dispatch

celsius=connector('Celsius')
fahrenheit=connector('Fahrenheit')

def converter(c,f):
    '''用约束条件连接C到f,将摄氏度转换为华氏度.'''
    u,v,w,x,y=[connector() for _ in range(5)]
    multiplier(c,w,u)
    multiplier(v,x,u)
    adder(v,y,f)
    constant(w,9)
    constant(x,5)
    constant(y,32)