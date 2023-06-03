import stdio

a=False
b=True

stdio.writeln(not(a and b) and (a or b) or ((a and b) or not (a or b)))

a=True
b=False

stdio.writeln(not(a and b) and (a or b) or ((a and b) or not (a or b)))
