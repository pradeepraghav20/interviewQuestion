
l=[4,4,3435,54,54,3,343,3]

for i in range(len(l)):
    for j in range(i+1,len(l)):
        if(l[i]>l[j]):
            temp=l[i]
            l[i]=l[j]
            l[j]=temp

print(l)



