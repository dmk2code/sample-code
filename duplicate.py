input_list = [401, 403, 409, 403, 453, 402, 438, 401, 444]
duplicate = []
unique = []

for i in input_list:
    if i in unique:
        duplicate.append(i)
    else:
        unique.append(i)
print("Duplicate Elements :", duplicate)


























