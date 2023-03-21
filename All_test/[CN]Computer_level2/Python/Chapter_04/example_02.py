import random
target=random.randint(1,1000)
count=0

while True:
    try:
        guess=int(input("请输入一个数字"))
    except:
        print("请输入数字,重试")
        continue
    count+=1
    if guess>target:
        print("猜大了")
    elif guess<target:
        print("猜小了")
    else:
        print("猜对了")
        break
print("猜测的次数是:",count)


