# Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).
#
#

# import re
# s='aasfdsgd sgd sg ds'
# # re.compile(r'[a-zA-Z0-9]')
# pattern=re.compile(r'[a-z]')
# res=pattern.search(s)
# print(res.group())


# import re
#
# target_string = "The price of PINEAPPLE ice cream is 20"
#
# # two groups enclosed in separate ( and ) bracket
# result = re.search(r"(\b[A-Z]+\b).+(\b\d+)", target_string)
#
# # Extract matching values of all groups
# print(result.groups())
# # Output ('PINEAPPLE', '20')



# 2. Write a Python program that matches a string that has an a followed by zero or more b's.
# import re
#
# patt=re.compile(r'^a(b*)$')
#
# # if patt.search("abbx"):
# #     print ("found")
#
# rs=patt.search("abbx")
# print(rs.groups())


# Write a Python program that matches a string that has an a followed by one or more b's


pattern='^a(b+)$'

# 5. Write a Python program that matches a string that has an a followed by three 'b'.


pattern=r'ab{3}'

#
# import re
# def text_match(text):
#         patterns = 'ab{3}'
#         if re.search(patterns,  text):
#                 return 'Found a match!'
#         else:
#                 return('Not matched!')
#
# # print(text_match("abbb"))
# print(text_match("aabbbbbc"))




# import re
# def text_match(text):
#         patterns = 'ab{2,3}'
#         if re.search(patterns,  text):
#                 return 'Found a match!'
#         else:
#                 return('Not matched!')
# print(text_match("ab"))
# print(text_match("aabbbbbc"))
#
# Write a Python program to find the sequences of one upper case letter followed by lower case letters.
#
# '[A-Z]+[a-z]+$'