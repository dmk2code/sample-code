#WAP replace each string from the given list with the same string which is repeated with length of the string.

def multiplay(mul):
    enter_input = int(input("range of input: "))
    in_put = []
    out = []
    for x in range(enter_input):
        x = input("enter elements: ")
        in_put.append(x)
    for y in in_put:
        z = len(y)
        z1 = z * y
        out.append(z1)
    print(out)


multiplay([])