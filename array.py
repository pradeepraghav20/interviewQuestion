# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,
#
# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this


list_expense=[2200,2350,2600,2130,2190]
print(list_expense)

#solution 1
print (list_expense[1]-list_expense[0])
#solution 2
print(sum(list_expense[0:3]))
#solution 3
# for i in range (len(list_expense)):
#     if list_expense[i]==2000:
#         print(i)


#solution 4

list_expense.append(1980)
print(list_expense)
#solution 5
list_expense[3]=list_expense[3]-200
#list_expense.insert(3,update_Val)
print(list_expense)


