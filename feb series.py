# # Python program to display the Fibonacci sequence
#
# # def recur_fibo(n):
# #    if n <= 1:
# #        return n
# #    else:
# #        return(recur_fibo(n-1) + recur_fibo(n-2))
# #
# # nterms = 10
# #
# # # check if the number of terms is valid
# # if nterms <= 0:
# #    print("Plese enter a positive integer")
# # else:
# #    print("Fibonacci sequence:")
# #    for i in range(nterms):
# #        print(recur_fibo(i))
#
#
#
# # def feb_generato(n):
# #     a,b=0,1
# #
# #     while(a<n):
# #         yield a
# #         a,b=b,a+b
#
#
# #
# # x=feb_generato(5)
# # for i in x:
# #     print (i)
#
# #
# # def feb_serires(n):
# #     if (n<=1):
# #         return n
# #     else:
# #         return feb_serires(n-1)+feb_serires(n-2)
#
# # def feb_series(n):
# #     a,b=0,1
# #     while(a<n):
# #         yield a
# #         a,b=b,a+b
# #
# # for i in feb_series(5):
# #     print(i)
#
# l=[4,4,3,3,3]
# res=list(filter(lambda a:a%2==0,l))
# print(res)
# res=[i for i in l if i%2==0]
# print(res)
#
#
#


# def rev_num(n):
#     sum=0
#     while(n!=0):
#
#         temp=n%10
#         sum=sum*10+temp
#         n=n//10
#     print(sum)
#
# rev_num(1012)




# def square(m):
#     for i in range(m):
#         yield i**2
#
#
#
# for i in square(10):
#     print(i)



