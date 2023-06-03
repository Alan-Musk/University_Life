import sys
import stdio
from bst import OrderedSymbolTable
# minLength:最短长度 minCount:计数阈值 bst:排序符号表
# word:当前单词 bst[word]:当前单词的位置数组
minLength=int(sys.argv[1])
minCount=int(sys.argv[2])

words=stdio.readAllStrings()
bst=OrderedSymbolTable()
for i in range(len(words)):
    word=words[i]
    if len(word)>=minLength:
        if word not in bst:bst[word]=[]
        bst[word]+=[i]

for word in bst:
    if len(bst[word])>=minCount:
        stdio.write(word+':')
        for i in bst[word]:
            stdio.write(str(i)+' ')
        stdio.writeln()