# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take
# from a user using input() function
#
# 1. Length of the list
# 2. Add 'black panther' at the end of this list
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)



heros=['spider man','thor','hulk','iron man','captain america']
print ("Lenght",len(heros))

heros.append('black panthe')
print(heros)
heros.pop()
index_of_hulk=heros.index("hulk")
heros.insert((index_of_hulk+1),"black panther")
# heros[2],heros[3]='octor' ,'strange'
heros[1:3]=["doctor strange"]
print(sorted(heros))

# odd_num=[]
# n=int(input("Enter Number"))
# for i in range(1,n):
#     if (i%2!=0):
#         odd_num.append(i)
#
# print(odd_num)

