numbers = [2, 3, 4, 4, 3, 1, 3, 2,  8]
unique = []
for number in numbers:
    if number not in  unique:
        unique.append(number)
        unique.sort()
print(unique)