from cs50 import get_int

scores=[]

for i in range(3):
    socre=get_int("Score:")
    scores.append(socre)

average=sum(scores)/len(scores)
print(f"Average:{average}")