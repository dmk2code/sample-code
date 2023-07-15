#Take two input strings from the user and concatenate two given strings by omitting the first character
def omit(frst):
    x = input("enter 1st string: ")
    y = input("enter 2nd string: ")
    output = x[1:] +" "+ y[1:]
    print(output)


omit([])