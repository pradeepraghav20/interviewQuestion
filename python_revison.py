# # def deco_func(mark_avg):
# #     def grade_fun(l):
# #         avg =mark_avg(l)
# #         if (avg>75):
# #             print ("First Devision")
# #         elif(avg<30):
# #             print ("Fail")
# #         mark_avg(l)
# #     return grade_fun
# #
# #
# #
# # @deco_func
# # def mark_avg(l):
# #     avg=sum(l)/len(l)
# #     return avg
# #
# # mark_avg([1,2,3])
#
#
#
# #list compe
# # compe
# # a=[3,4,43,5,6,7,6]
# #
# # res=[x for x in a if x%2==0]
# # print(res)
# #
#
# # try:
# #     pass
# # except:
# #     pass
# # else:
# #     pas
#
#
# try:
#     x=44
#     y=0
#     res=x%y
# except ZeroDivisionError as e:
#     print(e)
# else:
#     print("No Error")
#
#
# try:
#
#     a=[4,4]
#     iterator=iter(a)
#     print(next(iterator))
#     print(next(iterator))
#     print(next(iterator))
# except StopIteration:
#     pass
#
#



# def fact(n):
#     if (n==1):
#         return  n
#     else:
#         return n*fact(n-1)
#
# res=fact(5)
# print(res


#prime number
#
# def prime_num(n):
#     if (n>2):
#         for i in range(2,n):
#             if (n%i==0):
#                 print("Not Prime")
#                 break
#         else:
#             print("Prime")
#
#
# print(prime_num(72))

#
# def feb_series(n):
#     if (n<=1):
#         return  n
#     else:
#         return feb_series(n-1)+feb_series(n-2)
#
# print(feb_series(3))



# def feb_Series(n):
#     a,b=0,1
#     sum=0
#     for i in range(n):
#         print(sum)
#         a=b
#         b=sum
#         sum=a+b
#
# feb_Series(5)


