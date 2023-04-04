# # l=[3,2,1]
# # for i in range(0,len(l)):
# #     min_val=min(l[i:])
# #     min_ind=l.index(min_val)
# #     l[i],l[min_ind]=l[min_ind],l[i]
# # print(l)
#
#
#
# Input: x = 123
# Output: 321
# Example 2:
#
# Input: x = -123
# Output: -321
# Example 3:
#
# Input: x = 120
# Output: 21


def rev_num(n):
    rev_num=0
    while(n!=0):
        temp=n%10
        rev_num=rev_num*10+temp
        n=n//10
    return rev_num

n=int(input("value of n"))
if(n<0):
    res=rev_num(-(n))
    print (-(res))
else:
    print(rev_num(n))