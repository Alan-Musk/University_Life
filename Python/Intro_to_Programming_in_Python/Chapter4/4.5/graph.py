import sys
import stdio
from instream import InStream

class Graph:
    # 构造函数,传入参数:文件名,间隔符
    def __init__(self,filename=None,delimiter=None) -> None:
        self._e=0   # 边的数量
        self._adj=dict() # 新建一个空字典,不支持顺序相关操作
        if filename is not None:
            instream=InStream(filename) # 将文件中数据流传入instream中
            while instream.hasNextLine():# 判断是否为空行
                line=instream.readLine()# 逐行读取
                names=line.split(delimiter) # 按delimiter(默认为空字符)分割字符串
                for i in range(1,len(names)):
                    self.addEdge(names[0],names[i])
    # str函数
    def __str__(self) -> str:
        s=''
        for v in self.vertices(): # 遍历图中中所有顶点
            s+=v+' ' 
            for w in self.adjacentTo(v): # 遍历顶点v中所有邻居
                s+=w+' '
            s+='\n'
        return s    # return 图的字符串
    # 在图中从v到w添加一条边 隐含顶点生成
    def addEdge(self,v,w):
        if not self.hasVertex(v):self._adj[v]=set() # 生成顶点 将顶点self._adj[v]设为集合
        if not self.hasVertex(w):self._adj[w]=set() # 同
        if not self.hasEdge(v,w): # 判断两点之间有无边
            self._e+=1              # 图中边++
            self._adj[v].add(w)     # 顶点集合中+w顶点 用来输出邻居
            self._adj[w].add(v)     # 同
    # 遍历图中所有顶点
    def vertices(self):
        return iter(self._adj)
    # 遍历顶点v的所有邻居
    def adjacentTo(self,v):
        return iter(self._adj[v])
    # 判断v w是否为图中的一条边
    def hasEdge(self,v,w):
        return w in self._adj[v]
    # 图中顶点的总数
    def countV(self):
        return len(self._adj)
    # 图中边的总数
    def countE(self):
        return self._e
    # 顶点v的邻居数
    def degree(self,v):
        return len(self._adj[v])
    # v 是否为图中一个顶点
    def hasVertex(self,v):
        return v in self._adj
    
def main():
    file=sys.argv[1]
    graph=Graph(file)
    stdio.writeln(graph)

if __name__=='__main__':main()