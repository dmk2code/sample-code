#Write a program replace each string with an integer value in a given list of strings.
# The replacement integer value should be sum of ascci values of each character of the same string.
#holy_rivers = ["Ganges", "Godavari", "Bramhaputra", "Narmada", "yemuna", "Mahanadi", "Kaveri", "Tapati"]

def rivers(holy):
    holy_rivers = []
    for y in range(10):
        y = input("enter river name: ")
        holy_rivers.append(y)
    rivers = []
    for holy in range(len(holy_rivers)):
        x = str(holy)
        x = ord(x)
        rivers.append(x)
    return rivers


print(rivers([]))
