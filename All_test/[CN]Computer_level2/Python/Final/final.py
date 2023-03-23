def futureWeight(w,year):
    return w+0.5*year

def moonWeight(w):
    return w*0.165

while True:
    try:
        w=input("宇航员体重是:")
        if w in ["q","Q"]:
            break
        else:
            w=eval(w)
        print("{}年后,地球上的体重为:{}月球上的体重是:{}".format(10,futureWeight(w,10),moonWeight(w)))
    except:
        print("输入格式有误")