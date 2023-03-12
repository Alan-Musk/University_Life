import stdio
class Stack:
    def __init__(self) -> None:
        self._first=None
    def isEmpty(self):
        return self._first is None
    def push(self,item):
        self._first=_Node(item,self._first)
    def pop(self):
        item=self._first.item
        self._first=self._first.next
        return item
class _Node:
    def __init__(self,item,next) -> None:
        self.item=item
        self.next=next
def main():
    stack=Stack()
    while not stdio.isEmpty():
        item=stdio.readString()
        if item !='-':stack.push(item)
        else:stdio.write(stack.pop()+' ')
    stdio.writeln()

if __name__=='__main__':main()