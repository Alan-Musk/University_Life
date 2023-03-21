s=input("请输入一个字符串")

def isNum(s):
    try:
        complex(s)
        return True
    except:
        return False