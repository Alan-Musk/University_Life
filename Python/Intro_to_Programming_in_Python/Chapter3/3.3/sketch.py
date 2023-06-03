import sys
import stdarray
import stdio 
from vector import Vector

class Sketch:
    def __init__(self,text,k,d) -> None:
        freq=stdarray.create1D(d,0) # 哈希频率
        for i in range(len(text)-k):
            kgram=text[i:i+k]   # 文档中K个连续字符
            freq[hash(kgram)%d]+=1
        vector=Vector(freq)
        self._sketch=vector.direction()
    
    def similarTo(self,other):
        return self._sketch.dot(other._sketch)
    
    def __str__(self):
        return str(self._sketch)
    
def main():
    text=stdio.readAll()
    k=int(sys.argv[1])
    d=int(sys.argv[2])
    sketch=Sketch(text,k,d)
    stdio.writeln(sketch)

if __name__=='__main__':main()