def feb_serries(n):
    if (n<=1):
        return n
    else:
        return feb_serries(n-1)+feb_serries(n-2)



for i in range(10):

    res=feb_serries(i)
    print(res)