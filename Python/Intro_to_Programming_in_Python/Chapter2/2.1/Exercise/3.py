

def majoir(bo1,bo2,bo3):
    return (bo1 and bo2) or (bo2 and bo3) or (bo3 and bo1)

majoir(True,True,False)