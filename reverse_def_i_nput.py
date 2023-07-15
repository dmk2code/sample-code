#Write a program reverse each string from the given list and finally reverse a list.
def reverse(string):
    list_reverse = int(input("enter the range of elemnts: "))
    list_r = []
    reverse = []
    for x in range(list_reverse):
        x = input("enter the elements: ")
        list_r.append(x)
    for y in list_r:
        z = y[::-1]
        reverse.append(z)
    print(reverse)


reverse([])