import sys
import stdio 

class Stack:
    def __init__(self) -> None:
        self._a=[]
    def isEmpty(self):
        return len(self._a)==0
    def __len__(self):
        return len(self._a)
    def push(self,item):
        self._a+=[item]
    def pop(self):
        return self._a.pop()

def main():
    stack=Stack()
    while not stdio.isEmpty():
        item=stdio.readString()
        if item!='-':stack.push(item);
        else:stdio.write(stack.pop()+' ');
    stdio.writeln()

if __name__=='__main__':main()