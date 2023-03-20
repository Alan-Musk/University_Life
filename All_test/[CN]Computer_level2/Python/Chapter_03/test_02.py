input_string = input("请输入字符串：")  # 获取用户输入的字符串

# 将输入的字符串按照空格分割成列表
string_list = input_string.split(" ")

# 逐行打印出分割后的字符串
for string in string_list:
    print(string)
