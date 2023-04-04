
#
#
# def squear_num(n):
#     new_Num = 0
#     while (n != 0):
#         temp = n % 10
#         new_Num += temp ** 2
#         n = n // 10
#     return new_Num
#
# def happy_num(n):
#
#     seen=set()
#     while squear_num(n) not in seen:
#         sum1=squear_num(n)
#         if sum1==1:
#             return True
#         else:
#             n=sum1
#             seen.add(sum1)
#     return False
#
# print(happy_num(19))


def isHappy(n):
    def square_num(num):
       # num new_num = 0
       #  while (num > 0):
       #      temp = num % 10
       #      new_num = new_num + temp * temp
       #      num = num // 10
       sums = sum([int(digit) ** 2 for digit in str(n)])
       return sums

    seen = set()
    while square_num(n) not in seen:
        sum1 = square_num(n)
        if (sum1 == 1):
            return True
        else:
            seen.add(sum)
            n = sum1
    return False

print(isHappy(4))


def isHappy(self, n: int) -> bool:
    seen = set()  # to store all the sum of square if digits
    while n != 1:
        sums = sum([int(digit) ** 2 for digit in str(n)])  # sum of square of digits
        if sums in seen:  # if the sums in present in seen then it will be a endless loop
            return False
        n = sums
        seen.add(n)

    return True



