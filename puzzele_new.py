# Write a Python program to check whether the given strings are palindromes or not.
# Return True, False. Go to the editor
# Input:
# ['palindrome', 'madamimadam', '', 'foo', 'eyes']
# Output:
# [False, True, True, False, False]

def palidrome(l):
    # for i in l:
    #     temp_str=i
    #     if (temp_str==i[::-1]):
    #         yield True
    #     else:
    #         yield False
    return [s == s[::-1] for s in l]


l=['palindrome', 'madamimadam', '', 'foo', 'eyes']
for i in palidrome(l):
    print(i,end=" ")