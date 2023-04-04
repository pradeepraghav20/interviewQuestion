# 13. Write a Python program to find the strings in a given list, starting with a given prefix.
# Go to the editor
# Input:
# [( ca,('cat', 'car', 'fear', 'center'))]
# Output:
# ['cat', 'car']
# Input:
# [(do,('cat', 'dog', 'shatter', 'donut', 'at', 'todo'))]
# Output:


# def find_word(l):
#     for i in l:
#         for k in i[1]:
#             if(k.startswith(i[0])):
#                 print(k)






#
# l=[( 'ca',('cat', 'car', 'fear', 'center'))]
# find_word(l)




# Write a Python program to find the lengths of a given list of non-empty strings. Go to the editor
# Input:
# ['cat', 'car', 'fear', 'center']
# Output:
# [3, 3, 4, 6]
# Input:
# ['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
# Output:
# [3, 3, 7, 5, 2, 4, 0]
#
# l=['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
# res=[len(i) for i in l if len(i)>2]
# print(res)

#
# Write a Python program find the longest string of a given list of strings. Go to the editor
# Input:
# ['cat', 'car', 'fear', 'center']
# Output:
# center

# def max_str(l):
#     max_len=len(l[0])
#     for i in range(1,len(l)):
#         if (max_len<len(l[i])):
#             max_len=len(l[i])
#             res=i
#     return l[i]
#
#
#
l=['cat','center' 'car', 'fear']
res=max(l,key=len)
print(res)
# print(max_str(l))