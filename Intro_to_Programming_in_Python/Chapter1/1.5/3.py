import stdio

total=0.0
count=0

while not stdio.isEmpty():
    value=stdio.readFloat()
    total+=value
    count+=1
avg=total/count
stdio.writef('Average is %.2f\n',avg)