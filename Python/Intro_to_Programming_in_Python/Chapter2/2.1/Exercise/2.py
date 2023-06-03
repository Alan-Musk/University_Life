import stdio

def odd(bo1,bo2,bo3):
    if bo1 and bo2 and bo3:
        return True
    elif (bo1 and not bo2 and not bo3) or (bo2 and not bo1 and not bo3) or (bo3 and not bo1 and not bo2):
        return True
    else:
        return False

stdio.writeln(str(odd(True,False,False)))