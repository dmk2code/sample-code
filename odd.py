list = []
list1 = []
for x in range(10):
    x= input(">")
    list.append(x)
for y in list:
    if (len(y)%2!=0):
        list1.append(y)
print(list1)
