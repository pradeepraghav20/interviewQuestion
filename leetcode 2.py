# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
#
# Input: l1 = [0], l2 = [0]
# Output: [0]
#
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# l1 = [2,4,3]
# l2 = [5,6,4]

l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
if len(l1)==len(l2):

    l1.reverse()
    l2.reverse()
    new_num1=""
    new_num2=""
    for i in l1:
        new_num1+=str(i)

    for i in l2:
        new_num2+=str(i)

    print(int(new_num1)+int(new_num2))
else:
    l1.reverse()
    l2.reverse()
    new_num1 = ""
    new_num2 = ""
    for i in l1:
        new_num1 += str(i)

    for i in l2:
        new_num2 += str(i)

    num=int(new_num1) + int(new_num2)
    rev_num=0
    l=[]
    while(num!=0):
        temp=num%10
        rev_num=rev_num*10+temp
        num=num//10
    print(rev_num)
    while (rev_num!=0):
        temp = rev_num % 10
        l.append(temp)
        rev_num = rev_num // 10

    l.reverse()
    print(l)



