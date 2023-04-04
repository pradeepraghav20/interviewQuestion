def check_prime(n):
    if n<=1:
        return False
    else:
        for i in range (2,n):
            if n%i==0:
                return False
                break


        else:
            return True
#
# res=check_prime(7)
# print(res)
# # def check_prime_range(a,b):
# #     for i in range(a,b):
# #         if check_prime(i):
# #             print(i)
# #
# #
# # check_prime_range(10,20)




#arms