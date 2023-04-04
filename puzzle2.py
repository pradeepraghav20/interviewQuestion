# Write a Python program that accept a list of integers and check the length and the fifth element.
# Return true if the length of the list is 8 and fifth element occurs thrice in the said list. Go to the editor
# Input:
# [19, 19, 15, 5, 5, 5, 1, 2]
# Output:
# True
# Input:
# [19, 15, 5, 7, 5, 5, 2]
# Output:
# False
# Input:
# [11, 12, 14, 13, 14, 13, 15, 14]
# Output:
# True
# Input:

def check_list(l):
    if len(l)==8 and l.count(l[4])==3:return True

l=[19, 19, 15, 5, 5, 5, 1, 2]
l1=[19, 15, 5, 7, 5, 5, 2]

if check_list(l1) :
    print("True")
else:
    print("False")

