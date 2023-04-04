# # Write a program to find out all repeated numbers in a list.
# # array=[1,1,2,2,3]
#
# array=[1,1,2,2,3]
# {1:2,2:2,3:1}


# array=[1,1,2,2,3]
# count_num={}
#
# for i in array:
#     count_num[i]=array.count(i)
#
# print(count_num)


# Write a program to find all smaller elements from an existing element in a list
# array=[8,4,5,2,1]
#
# output:
# {8:4,4:2,5:3,2:1,1:0}

# array=[8,4,5,2,1]
#
# min=array[0]
#
# for i in array:
#     if i<min:
#         min=i

# print(min)


# Write a program to find out all possible combinations of a string
# str="abcd"
#
# output:
# ['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca',
#  'cabd', 'cadb',
#  'cbad', 'cbda', 'cdab', 'cdba', 'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba']
import itertools

str="abcd"
import  itertools
l=list(str)
res=list(itertools.permutations(l))
print(res)
# for i in res:
#     print("".join(i))
print(["".join(i) for i in res])