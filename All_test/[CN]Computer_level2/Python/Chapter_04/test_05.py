import random

# 模拟参赛者坚持选择的情况
def no_change():
    doors=['goat','goat','car']
    # 参赛者一开始以随机选择一扇门
    choice=random.choice(doors)
    # 主持人选择其中一扇门,露出山羊
    doors.remove('goat')
    if choice=='car':
        return 1
    else:
        return 0
    
def change():
    doors=['goat','goat','car']
    choice=random.choice(doors)
    doors.remove('goat')
    choice=random.choice(doors)
    if choice=='car':
        return 1
    else:
        return 0
    
n=10000
no_change_wins=0
change_wins=0

for i in range(n):
    no_change_wins+=no_change()
    change_wins+=change()

print("不更换选择获胜的概率是:",no_change_wins/n)
print("更换选择获胜的概率是:",change_wins/n)