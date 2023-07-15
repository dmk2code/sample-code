#Write a program change the given input list by  doing rotate left
#output - [5,6,7,4]

def rotate(num):
    x = [4, 5, 6, 7]
    y = x[0]
    x.pop(0)
    x.append(y)
    print(x)


rotate([])