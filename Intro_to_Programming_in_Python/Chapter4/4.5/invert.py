import sys
import stdio
from graph import Graph

file=sys.argv[1]
delimiter=sys.argv[2]
graph=Graph(file,delimiter)

while stdio.hasNextLine():
    v=stdio.readLine()
    if graph.hasVertex(v):
        for w in graph.adjacentTo(v):
            stdio.writeln('   '+w)
            