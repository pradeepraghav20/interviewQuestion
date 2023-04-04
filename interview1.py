#decorater

# def deco_grade(cal_avg):
#     def set_grade(marks):
#         avg_marks=cal_avg(marks)
#         if (avg_marks>90):
#             print("Grade is-",'A')
#         else:
#             print("Grade is-", 'B')
#
#         return cal_avg(marks)
#     return set_grade
#
# @deco_grade
# def cal_avg(marks):
#     sum_marks=sum(marks)
#     avg_marks=sum_marks/len(marks)
#     print("Average Marks-",avg_marks)
#     return avg_marks
#
# marks=[10,20,30,40,50]
# cal_avg(marks)
#
#
#
#
#Generator and iterator

def square(n):
    for i in range(1,n):
        return  i*i

def squaare_fun(n):
    for i in range(1, n):
        yield i*i

res=squaare_fun(5)
print(next(res))
print(next(res))




