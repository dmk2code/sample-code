#Write a program convert the following list to a dictionary.
#Note: Please don’t use dict() function.
def dic(**x):
    keys = []
    values = []
    for x in range(5):
        x = input("Enter Keys: ")
        keys.append(x)
    for y in range(5):
        y = input("Enter Values: ")
        values.append(y)
    res = {keys[i]: values[i] for i in range(len(keys))}
    return res


print(dic())
