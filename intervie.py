# l=[4,4,3,3343,5,6,66,4,4,3,33,45,5]
# new_even=[]
# for i in l:
#     if i%2==0:
#         new_even.append(i)
#
# print(new_even)
#
# res=list(filter(lambda a:a%2==0,l))
# l=[4,4,3,3343,5,6,66,4,4,3,33,45,5]
# res=[x for x in l if x%2==0]

# records = []
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     student = []
#     student.append(name)
#     student.append(score)
#
#     records.append(student)
#     del student

l=[10, 13, 17, 11, 34, 21]
import math
min=l[0]
for i in range(1,len(l)):
    if min>l[i]:
        min=l[i]
sec_min=math.inf
print(min)
for i in range(0,len(l)):
    if l[i]< sec_min and l[i]!=min:
        sec_min=l[i]


