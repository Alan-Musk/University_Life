etxt=input("加密后的文本")
for p in etxt:
    if "a"<=p<="z":
        print(chr(ord("a")+(ord(p)-ord("a")-3)%26),end='')
    elif "A"<=p<="Z":
        print(chr(ord("A")+(ord(p)-ord("A")-3)%26),end='')
    else:
        print(p,end='')