def isPrime(num):
    if not isinstance(num,int):
        raise TypeError("输入的参数必须为整数")
    if num < 2:
        return False
    for  i in range(2,int(num**0.5)+1):
        if num %i==0:
            return False
    return True