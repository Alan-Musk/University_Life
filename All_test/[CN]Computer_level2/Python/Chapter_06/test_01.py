t=input("请输入一段字符串")
t=t.lower()
dic={}
for i in t:
    dic[i]=dic.get(i,0)+1
items=list(dic.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in items:
    word,count=i[0],i[1]
    print("{0:<10}{1:>5}".format(word,count))