#names = "manikanta"
#def wish_me(wish, compose):
    #return f"{wish} {names} {compose}"
#gap = wish_me("hi", 'how r u')
#print(gap)
#gap.isdigit

 #Subtract two lists with for loops
list1 = [10, 11, 12]
list2 = [1, 2, 3]
subtracted = []
for item1, item2 in zip(list1, list2):
    item = item1 - item2
    subtracted.append(item)
print(subtracted)
# Returns: [9, 9, 9]
