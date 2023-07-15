#Write a program find all even numbers from the given list.

def even(eve):
    input_list = []
    output = []
    for x in range(10):
        x = int(input("</>"))
        input_list.append(x)
    for z in input_list:
            if z % 2 == 0:
                output.append(z)
    return output



print(even([]))