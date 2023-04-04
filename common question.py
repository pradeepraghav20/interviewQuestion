# feb series
# def feb_series(n):
#     if (n<=1):
#         return n
#     else:
#         return feb_series(n-1)+feb_series(n-2)
#
#
# for i in range(5):
#     print (feb_series(i),end=" ")


# def feb_Series(n):
#     a,b=0,1
#     while(a<n):
#         yield a
#         a,b=b,a+b
#
#
# for i in feb_Series(5):
#     print(i)



#revseresr number
# def rev_num(n):
#     sum=0
#     while(n!=0):
#         temp=n%10
#         sum=sum*10+temp
#         n=n//10
#
#     print(sum)
# n=124
#
# rev_num(n)


#string palindrome
#
# s="pradeep"
# rev_str=s[::-1]
# print(rev_str)
#
#
# sort_array

# a=[3,4,4,3,3,3,2,-2]
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]>a[j]:
#             temp=a[i]
#             a[i]=a[j]
#             a[j]=temp
#
# print(a)

