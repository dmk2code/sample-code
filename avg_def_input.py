#WAP find the average of given list of elements representing a grade of student.
#grades = [84, 84, 93, 78, 86, 73]
#Note: Please don’t use sum() function to add the elements from a list
def avg_grade(grades):
    for x in range(10):
        x = input(">>")
        grades.append(x)
    total = 0
    for y in grades:
        total += int(y)
        avg = total/len(grades)
    return avg

print("grade of student",avg_grade ([]) )