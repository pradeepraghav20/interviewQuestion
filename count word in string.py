s="Amazon Smartphone Upgrade Days AMazon Amaz Amazon Amazon v v v Amazon  on"
new_s=s.split()
print(new_s)
l=['Amazon','AMazon','AMazon']
c=0
for i in new_s:
    if i in l:
        c+=1
        print(i)

print(c)


l=[2,3,4,5,6,7]
print(len(l))
n=len(l)//3
sum=0
while n:

    l.remove(max(l))
    sum+=max(l)
    l.remove(max(l))
    l.remove(min(l))
    n=n-1

print(sum)

