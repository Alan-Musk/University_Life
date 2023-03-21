def prime(num):
    global numbers
    numbers=[True]*(num+1)
    numbers[0]=numbers[1]=False

    for i in range(2,int(num**0.5)+1):
        if numbers[i]:
            for j in range(i*i,num+1,i):
                numbers[j]=False
    primes=[i for i in range(2,num+1) if numbers[i]]
    print(primes)

prime(200)
