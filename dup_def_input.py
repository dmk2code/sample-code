#WAP print all duplicated values in descending order from the given input list

def dup(xerox):
    input_list = []
    duplicate = []
    unique = []
    for x in range(10):
        x = int(input("please enter the element:"))
        input_list.append(x)
    for i in input_list:
        if i in unique:
            duplicate.append(i)
        else:
            unique.append(i)
    xerox = "Duplicate Elements :"+ str(duplicate)
    return xerox


print(dup([]))
