#Write a program take 10 input strings of different lengths from the user and
# store all the strings into a list and display only odd length strings are the output in a list format.

def odd(length):
    list = []
    list1 = []
    for x in range(10):
        x = input(">")
        list.append(x)
    for y in list:
        if (len(y) % 2 != 0):
            list1.append(y)
    print(list1)


odd([])