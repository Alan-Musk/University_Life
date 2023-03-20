# 获取输入的数字
num = int(input("请输入一个数字(1-7): "))

# 定义星期字符串列表
weekdays = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]

# 输出对应的星期字符串名称
if num >= 1 and num <= 7:
    print(weekdays[num-1])
else:
    print("请输入1-7之间的数字")
