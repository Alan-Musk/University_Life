import stdio

def areTrigngular(num1,num2,num3):
    if (num2+num1)>num3 and (num1+num3) >num2 and (num2+num3)>num1:
        return True
    else:
        return False
    
stdio.writeln(areTrigngular(10,18,10))