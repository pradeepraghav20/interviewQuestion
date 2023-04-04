# s="1244"
# print(s[::-1])
#
# num=123
# sum=0
# while(num!=0):
#
#     temp=num%10
#     sum=sum*10+temp
#     num=num//10
#
# print(sum)



num=24
sum=0
for i in range(1,num):
    if (num%i==0):
        sum+=i

if (num==sum):
    print("Yes perfect number")