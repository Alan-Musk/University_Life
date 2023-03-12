import sys
import stdio
from instream import InStream
from hashst import SymbolTable

instream=InStream(sys.argv[1])
keyField=int(sys.argv[2])
valField=int(sys.argv[3])

database=instream.readAllLines()

st=SymbolTable()    # 创建 键值字典
for line in database:
    tokens=line.split(',')
    key=tokens[keyField]
    val=tokens[valField]
    st[key]=val
while not stdio.isEmpty():
    query=stdio.readString()
    if query in st:stdio.writeln(st[query])
    else:stdio.writeln('Not found')