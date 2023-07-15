#Write a program take input strings of equal length and the length of strings
# should be greater than 5 and display the output by combining last three characters
# from the 1st string with first three characters from the second string.

def str(strng):
    input_str1 = "PYTHON"
    input_str2 = "PROGRAMMING"
    x = input_str1[3:]
    y = input_str2[0:3]
    z = x + y
    print(z)


str([])