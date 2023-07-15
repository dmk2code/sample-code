#Write a program find the maximum number from the given input list
def max(num):
    input_list = [82, 62, 61, 54, 71, 89, 75, 73]
    max_num = input_list[0]
    for x in input_list:
        if x > max_num:
            max_num = x
            print(max_num)
            

max([])