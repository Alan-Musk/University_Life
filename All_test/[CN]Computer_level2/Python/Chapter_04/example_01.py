import random
target=random.randint(1,1000)
count=0

while True:
    guess=int(input("请输入一个数字"))
    count+=1
    if guess>target:
        print("猜大了")
    elif guess<target:
        print("猜小了")
    else:
        print("猜对了")
        break
print("猜测的次数是:",count)


