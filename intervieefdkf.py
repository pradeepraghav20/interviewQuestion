def square(n):
    for i in range(1,n):
        yield i*i

# res=square(10)
for i in square(10):
    print(i)
#
# def deco_squear(square):
#     def square_num(n):
#         print ("Square of number- ",n**2) #
#         return square(n)
#     return square_num
#
# @deco_squear
# def square(n):
#     print ("Number is-",n)
#
# square(5)


# l=[4,4,4,4,4]
# res=iter(l)
#
#
#
