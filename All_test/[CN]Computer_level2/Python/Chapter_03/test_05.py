decimal = int(input("请输入一个十进制整数: "))

binary = bin(decimal)
octal = oct(decimal)
hexadecimal = hex(decimal)

print(f"二进制：{binary}")
print(f"八进制：{octal}")
print(f"十六进制：{hexadecimal}")
