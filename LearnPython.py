# %%
# Print String 5 times
for i in range(5) :
     print("This is fun")





# %%
# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

print(newlist)






# %%
#Print all items in the list, one by one:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
     print(x)     





# %%
#Print all items by referring to their index number:
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
     print(thislist[i])




# %%
#Print all items, using a while loop to go through all the index numbers
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
     print(thislist[i])
     i = i + 1




# %%
