# Write a Python program find a list of integers with exactly two occurrences of nineteen and at least
# three occurrences of five. Go to the editor
# Input:
# [19, 19, 15, 5, 3, 5, 5, 2]
# Output:
# True
# Input:
# [19, 15, 15, 5, 3, 3, 5, 2]
# Output:
# False

def find_list(num_list):
    coont_19=num_list.count(19)
    count_5=num_list.count(5)
    # if coont_19==2 and count_5>=3:
    if num_list.count(19)==2 and num_list.count(5)>=3:
        return True

l=[19, 19, 15, 5, 3, 5, 5, 2]
l1=[19, 15, 15, 5, 3, 3, 5, 2]

if find_list(l):
    print ("Yess")
else:
    print("False")

