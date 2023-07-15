input_list = [18.8, "Hyd", 18, 26.9, 19, "BANG", 26, 33.7, 25, "CHEN"]
y = []
output = []
y.append(input_list[2])
y.append(input_list[4])
y.append(input_list[6])
y.append(input_list[8])
for z in y:
    if z % 2 == 0:
        output.append(z)
print(output)




