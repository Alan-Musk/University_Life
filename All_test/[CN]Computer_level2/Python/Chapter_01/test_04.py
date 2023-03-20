hobbies=""
for i in range(3):
    s=input('请输入你的小爱好')
    if s.upper()=='Q':
        break
    hobbies+=s
print("你的小爱好是:",hobbies)