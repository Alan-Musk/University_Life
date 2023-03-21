s=input("请输入字符串")

num_alpha=0
num_digit=0
num_space=0
num_other=0

for ch in s:
    if ch.isalpha():
        num_alpha+=1
    elif ch.isdigit():
        num_digit+=1
    elif ch.isspace():
        num_space+=1
    else:
        num_other+=1
print("英文字符个数：", num_alpha)
print("数字个数：", num_digit)
print("空格个数：", num_space)
print("其他字符个数：", num_other)

