f=open("abc",'r')
res=f.readlines()
f.read()
f.close()
with open("abc",'r') as file:
    print(file.read())