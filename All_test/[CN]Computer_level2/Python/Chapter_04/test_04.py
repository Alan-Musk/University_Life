import random

num=random.randint(1,1000)
count=0
while True:
    try:
        guess=int(input("请输入一个整数"))
    except:
        print("请输入一个整数")
        continue
    count+=1
    if guess>num:
        print("猜大了")
    elif guess<num:
        print("猜小了")
    else:
        print("猜对了")
        break
print("猜了:",count,"次")