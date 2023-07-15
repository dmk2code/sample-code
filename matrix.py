list = []
row, col = 3,3
for x in range(3):
     x=input(">")
     list.append(x)
for i in range(row + col):
     result = []
     for j in range(row):
          for k in range(col):
               if i == j + k:
                    result.append(list[j][k])





















