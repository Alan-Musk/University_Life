# _first:队列中第一个节点 _last:队列中最后一个节点 _n:队列中项目的个数
class Queue:
    def __init__(self) -> None:
        self._first=None
        self._last=None
        self._n=0

    def isEmpty(self):
        return self._first is None
    # 进人队列
    def enqueue(self,item):
        oldLast=self._last # 将最后一个节点复制给oldLast  
        self._last=_Node(item,None) # 新设置一个节点成为队列最后一个节点
        if self.isEmpty():self._first=self._last # 如果原队列为空,将最后节点地址赋值给第一个节点
        else:oldLast.next=self._last    # 不为空:将队列最后一个节点赋值给上一节点指向下一节点
        self._n+=1  # 队列总数+1
    # 删除队列
    def dequeue(self):
        item=self._first.item   
        self._first=self._first.next
        if self.isEmpty():self._last=None
        self._n-=1
        return item
    
    def __len__(self):
        return self._n

class _Node:
    def __init__(self,item,next) -> None:
        self.item=item
        self.next=next