matrix = []
for x in range(3):
    x = input(">>")
    matrix.append(x)
for y in matrix:
    result = 0
    for a in range(len(matrix)):
        for b in range(len(matrix[a])):
            if a == b:
                c = matrix[a][b]
        result = result + int(c)
    print(y)
print("the sum of digonal:"+str(result))