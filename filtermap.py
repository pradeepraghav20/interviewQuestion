l=[4,4,4,4,3,3]
# for i in l:
#     print (i**2)

res=list(map(lambda  a:a**2,l))
print(res)

l=[4,5,6,7,8,8]
res=list(filter(lambda x:x%2==0,l))
print(res)


from functools import reduce

l=[4,4,4,3,3,2,2]

res=reduce(lambda x,y:x+y,l)
print(res)