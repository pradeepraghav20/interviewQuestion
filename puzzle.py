# # We are making n stone piles! The first pile has n stones. If n is even, then all piles have
# # an even number of stones. If n is odd, all piles have an odd number of stones. Each pile must more stones than
# # the previous pile but as few as possible.
# # Write a Python program to find the number of stones in each pile. Go to the editor
# # Input: 2
# # Output:
# # [2, 4]
# # Input: 10
# # Output:
# # [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
# # Input: 3
# # Output:
# # [3, 5, 7]
#
#
# n=int(input())
# even_list=[]
# odd_list=[]
# if (n%2==0):
#     temp=n
#     for i in range(n):
#         even_list.append(temp)
#         temp+=2
# else:
#     temp = n
#     for i in range(n):
#         odd_list.append(temp)
#         temp += 2
#
# # def test(n):
# #
# #     return [n + 2 * i  for i in range(n)]
# #
# # print(test(3))
#
#
# print(even_list)
# print(odd_list)

def differ_num(l):
    for i in range(len(l)):
        # for j in range(i+1,len(l)):l
            if l[i+1]-l[i]==10:
                return True
            else:
                return False






l=[0,10,20,30]
res=differ_num(l)
print(res)