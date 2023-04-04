#
#
# l=[4,4,4,4,[4,[404],4,3],670,4,4,[44,4]]
# max=0
# new_list=[]
# for i in l:
#     if type(i) is list:
#         for k in i:
#             if k>max:
#                 max=k
#     else:
#         if i>max:
#             max=i
#
#
# print(max)
#
# # for i in l:
# #     if type(i) is list:
# #         new_list.extend(i)
# #     else:
# #         new_list.append(i)
# #
# # print(max(new_list))



l2=[]
def get_max(l):
    for i in l:
        if type(i) is list:
            get_max(i)
        else:
            l2.append(i)

    return max(l2)

