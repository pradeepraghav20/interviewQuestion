# l=[2,3,4,3,3,3]
# new_l=[]
# for i in range(0,len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]<=l[j]:
#             break
#     print(l[i])
#

# Python Function to print leaders in array

def printLeaders(arr, size):
    for i in range(0, size):
        for j in range(i + 1, size):
            if arr[i] <= arr[j]:
                break
        if j == size - 1:  # If loop didn't break
            print(arr[i], end=' ')


# Driver function
arr = [16, 17, 4, 3, 5, 2]
printLeaders(arr, len(arr))
