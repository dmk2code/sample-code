#Write a program find all even number from the given input list and display output as a list format
def even(eve):
    list = []
    final = []
    for x in range(10):
        x = input("Enter The Elements : ")
        list.append(x)
    for even in list:
        even = int(even)
        if even % 2 == 0:
            final.append(even)
    return final


print(even([]))