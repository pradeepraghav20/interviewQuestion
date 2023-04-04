# #sum of all the item in list
# l=[3,4,5,6,7,77]
# print (sum(l))
#
# sum1=0
# for i in (l):
#     sum1+=i
#
# print(sum1)


#Write a Python program to multiply all the items in a lis

# l=[3,4,5,6,7,77]
# mul=1
# for i in l:
#     mul*=i
# print(mul)
# #Write a Python program to get the largest number from a list
# l=[3,4,5,6,7,747]
# print(max(l))
# max=l[0]
# for i in range(len(l)):
#     if max<l[i]:
#         max=l[i]
#
# print(max)


# Write a Python program to get the smallest number from a list
# l=[3,4,5,6,7,747]
# min=l[0]
# for i in l:
#     if min>i:
#         min=i
#
# print(min)


# minWrite a Python program to count the number of strings where the string length is 2 or more and the first and
# last character are same from a given list of strings. Go to the editor
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

# List =['abc', 'xyz', 'aba', '1221']
#
# count =0
# for i in List:
#     if (len(i)>1 and i[0]==i[-1]):
#         count+=1
#
#
#
# print(count)
#


# Write a Python program to get a list, sorted in increasing order by the last element in each tuple
# from a given list of non-empty tuples. Go to the editor
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]



#Write a Python program to remove duplicates from a list

l=[3,4,4,4,45,6,7,747]
print (set(l))
for i in l:
    if l.count(i)>1:
        l.remove(i)

print(l)

l=[33]
if l:
  print ("Mot empty ")
else:
    print('Empty list')