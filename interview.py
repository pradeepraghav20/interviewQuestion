# # input = [1, 3, [2,3.4], 25, [2], "Hello"]
# # [1,3,2,3,4,25,2,"Hello"]
#
#
# input1 = [1, 3, [2,3.4], 25, [2], "Hello"]
# res=[]
#
# for i in input1:
#     print(i)
#     if type(i) is list:
#         for k in i:
#             res.append(k)
#     else:
#         res.append(i)
# print(res)

# import re
# input = "Hello 2022, this is 6 of oct"
#
# res=re.findall('\d{4}.',input)
# print(res)
#
input = "Hello 2022, this is 6 of oct"

for i in input:
    if i.isdigit():
        print(i ,end=" ")





