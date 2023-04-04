# # # # #palindrome string
# # # # # s="nitin"
# # # # # rev_str=s[::-1]
# # # # # if (rev_str==s):
# # # # #     print("Yess It's palindrome")
# # # # # else:
# # # # #     print("No It is not palindrome")
# # # # #
# # # # # #by using indexing or for loop
# # # #
# # # # def palindrome(s):
# # # #     n = len(s)
# # # #     for i in range(n):
# # # #         if (s[i]!=s[n-i-1]):
# # # #             return False
# # # #     return True
# # # #
# # # # print(palindrome("nitin"))
# # # # nitin
# # #
# # #
# # # #palindrome number
# # #
# # # # n=121
# # # # temp=n
# # # # sum=0
# # # # while(n!=0):
# # # #
# # # #     temp=n%10
# # # #     sum=sum*10+temp
# # # #     n=n//10
# # # #
# # # #
# # # # if temp==n:
# # # #     print("Yes")
# # # # else:
# # # #     print("Noo")
# # #
# # # #
# # #
# # #
# # # # def feb_rec(n):
# # # #     if n<=1:
# # # #         return n
# # # #     else:
# # # #         return feb_rec(n-1)+feb_rec(n-2)
# # # #
# # # # for i in range(5):
# # # #     res=feb_rec(i)
# # # #     print(res)
# # #
# # #
# # # # resl=[3,3,3,3,34,4,44,3]
# # # # d={}
# # # # for i in l:
# # # #     d[i]=l.count(i)
# # # #
# # # # print(d)
# # #
# # # #
# # # # s="aabbccddee"
# # # # d={}
# # # # l=list(s)
# # # # for i in l:
# # # #     d[i]=l.count(i)
# # # #
# # # # print(d)
# # #
# # #
# # # for num in range(1,n):
# # #
# # #     if (num%3==0):
# # #         print("Fizz")
# # #     elif (num%5==0):
# # #         print("Buzz")
# # #     elif (num%15==0):
# # #         print("BizzFIZZ")
# # #     else:
# # #         print (num)
# #
# #
# # def prime(n):
# #     if n>1:
# #         for i in range(2,n//2+1):
# #             if n%i==0:
# #                 break
# #         else:
# #             print(n,"Yess it is")
# #     # else:
# #     #     print ("not valid number")
# #
# # for i in range(10):
# #     prime(i)
#
# s="This_Is_Good_Morning"
# new=s.split("_")
# new_l=[]
# for i in new:
#     new_l.append(i.swapcase())
#
# print(".".join(new_l))
#

def fact(n):
    f = 1
    for i in range(1,n+1):
        f=f*i

    print(f)

def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)
print (fact(5))

