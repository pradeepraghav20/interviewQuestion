# Input: x = -121
# Output: false
# # Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome


num=int(input())
rev_num=0
while(num!=0):
    tem=num%10
    rev_num=num*10+tem
    num=num//10

print(rev_num)