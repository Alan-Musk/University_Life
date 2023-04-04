'''这一题,问的是哪个概率更大,是6中1,还是12中2,书上都没有说清楚,总之,感谢浪费我宝贵的时间'''
import random
import stdio

def dice(n):
    num=0
    for i in range(n):
        if random.randrange(1,7)==1:
            num+=1
    return num

trials=int(input("请输入要模拟的次数"))
sum_six=0 # 6中1的总和
sum_12=0 # 12中2的总和
for i in range(trials):
    if dice(6)>=1:
        sum_six+=1
    if dice(12)>=2:
        sum_12+=1
    
stdio.writeln("6中1的概率是{:5f}\n12中2的概率是{:.5f}".format(sum_six/trials,sum_12/trials))