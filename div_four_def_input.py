#Write a program create a random list of length 10 and
# print all the elements except the elements which are divisible by 4.

def div(four):
    four = int(input("Enter range of string: "))
    in_put = []
    out = []
    for y in range(four):
        y = input("please enter a string: ")
        in_put.append(y)
    for x in in_put:
        if len(x)%4==0:
            out.append(x)
    else:
        print("sorry, there is no string with div by 4.")

    return out


print(div(()))


