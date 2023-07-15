#Write a program create a infinite loop, for each loop execution prompt the user input, If
# suppose user enters other than integer come out of the loop and display all user entered values as list.
# (use while loop to create infinite loop)


final = []
while True:
    num = input(">")
    if num in "abcdefghijklmnopqrstuvwxyz":
        break
    else:
        final.append(num)
print(final)