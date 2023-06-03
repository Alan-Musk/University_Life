import stdio

for a in range(3,10):
    for b in range(3,10):
        for c in range(3,10):
            for d in range(3,10):
                for e in range(3,10):
                    if pow(a,5)+pow(b,5)+pow(c,5)+pow(d,5)==pow(e,5):
                        print("a={},b={},c={},d={},e={}".format(a,b,c,d,e))
