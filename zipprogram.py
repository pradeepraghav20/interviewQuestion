def check_prime(n):
    if (n<1):
        return False
    else:
        for i in range(2,n):
            if (n%i==0):
                return False
                break
        else:
            return True


if check_prime(0):
    print("Number is primer")
else:
    print("Number is not prime")
