# # def binary_search(l,n):
# #     l1=0
# #     u=len(l)-1
# #     while(l1<=u):
# #         mid=(u+l1)//2
# #         if l[mid]==n:
# #             return mid
# #         else:
# #             if l[mid]<n:
# #                 l1=mid+1
# #             else:
# #                 u=mid-1
# #     else:
# #         return False
#
#
#
#
# def binary_search(l,n):
#     lb=0
#     ub=len(l)-1
#     while(lb<=ub):
#         mid=(lb+ub)//2
#         if (l[mid]==n):
#             return True
#         else:
#             if (l[mid]<n):
#                 lb=mid+1
#             else:
#                 ub=mid-1
#     return False
#
# lst1=[3,4,5,6,6,6,7]
# res=binary_search(lst1,71)
# print(res)