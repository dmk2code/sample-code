#Given a string of even length and print
# the output as string contains last half added with first half of the given string
def even(eve):
    string = []
    for x in range(1):
        x = input(">>")
        if len(x)%2==0:
            string.append(x)
        else:
            print("please enter even length str")
    for y in string:
        a = y[0:3]
        b = y[3:]
        ab = b+a
        return ab

print(even([]))