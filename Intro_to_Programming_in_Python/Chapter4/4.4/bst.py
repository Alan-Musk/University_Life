class OrderdSymbolTable:
    # 构造函数
    def __init__(self) -> None:
        self._root=None
    # 内部的get函数 x:BST根 key:键
    def _get(self,x,key):
        if x is None:raise KeyError
        if key<x.key:return self._get(x.left,key)
        elif x.key<key:return self._get(x.right,key)
        else:return x.val
    
    def __getitem__(self,key):
        return self._get(self._root,key)
    # 内部的set函数 x:BST根,key:键 val:值
    def _set(self,x,key,val):
        if x is None:return _Node(key,val)
        if key<x.key:x.left=self._set(x.left,key,val)
        elif x.key<key:x.right=self._set(x.right,key,val)
        else:x.val=val
        return x

    def __setitem__(self,key,val):
        self._root=self._set(self._root,key,val)


class _Node:
    def __init__(self,key,val) -> None:
        self.key=key
        self.val=val
        self.left=None
        self.right=None