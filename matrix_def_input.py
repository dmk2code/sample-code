#Write a program create 3x3 matrix using python. Take all the elements from the user.
# And also print the sum of diagonal elements from created matrix.
def matrix(result):
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
    return result


print(matrix([]))

