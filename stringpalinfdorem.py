# s="pradeep"
# temp=s
# if (temp==s[::-1]):
#     print("Yess")
# else:
#     print ("Noo")
#
#
# s1=list(s)
# print("".join(reversed(s1)))
#


def feb(num):
    if num<=1:
        return num
    else:
        return (feb(num-1)+feb(num-2))


print(feb(3))





def fact(n):
    sum = 1
    for i in range(1,n+1):
        sum=sum*i
    print(sum)


fact(5)