
def letter(s):
    global num_alpha,num_other,num_space,num_digit
    num_alpha=0
    num_digit=0
    num_space=0
    num_other=0
    for ch in s:
        if ch.isspace():
            num_space+=1
        elif ch.isalpha():
            num_alpha+=1
        elif ch.isdigit():
            num_digit+=1
        else:
            num_other+=1
s=input("请输入一个字符串")
letter(s)
print("字母有:  ",num_alpha)
print("数字有:  ",num_digit)
print("空格有:  ",num_space)
print("其他有:  ",num_other)
