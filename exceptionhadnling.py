# age=13
# class MyException(Exception):
#     pass
# try:
#
#     if age <18:
#         raise MyException ("not vaild")
# except MyException as e:
#     print(e)


l=[3,4,4,4,44,4]
l2=[4,4,3,3,3,3]


l.extend(l2)
print(l)