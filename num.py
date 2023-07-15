#def my_function(fname):        ARGUMENTS
 #   print(fname + " refenses")

#my_function("mani" )
#my_function("sai" )
#########################
#def my_function(**kid):
 # print("His last name is " + kid["lname"])
#my_function(fname = "Tobias", lname = "Refsnes")
########################################
#thislist = ["apple", "banana", "cherry"]
#i = 0
#while i < len(thislist):
 # print(thislist[i])
  #i = i + 1
 #
#values = [16, 1, 7, 2, 19, 12, 5, 20, 2, 10, 10, 14, 17, 14, 1, 16, 19, 7, 9, 19]
#for x in range(len(values)):
 #   values[x]+=1
  #  print(x)

  #################################################
#values = [16, 1, 7, 2, 19, 12, 5, 20, 2, 10, 17, 14, 1, 9]
# Write your answer below
#reversed_values = []
#for x in range(len(values)):
 #   reversed_values.append(values[-x -1])
  #  print(reversed_values)
  ####################
#values = [3, 5, 2, 1]

#total = 0
#for x in values:
 #   total += x
  #  print(total)
   # answer_x = x
    #print(answer_x)
    #answer_total = total
    #print(answer_total)


#Write a Python program that calculates the number of rows and columns of the matrix stored in variable matrix.
#Assign the number of rows to a variable named num_rows and the number of columns to a variable named num_cols.

#matrix = [
 #   [0, 9, 5, 4, 5, 3, 1, 5, 7],
  #  [8, 2, 1, 7, 3, 1, 5, 7, 0],
   # [1, 5, 3, 2, 7, 1, 4, 4, 8],
    #[2, 5, 6, 2, 0, 4, 1, 9, 3],
    #[7, 4, 2, 9, 7, 0, 7, 4, 4],
#]

# Write your code below
#num_rows = len(matrix)
#num_cols = len(matrix[0])
#print(num_cols)
#print(num_rows)

####SUM OF MATRIX####
#matrix = [
 #   [0, 9, 5, 4],
  #  [8, 2, 3, 0],
   # [1, 5, 3, 2]
#]

# Write your code below
#num_cols = len(matrix[0])
#otal =0
#for row in range(num_rows):
 #   for col in range(num_cols):
  #      total+=matrix[row][col]
   #     print(total)

#stars = '*'
#stars += stars
#stars += stars
#stars += stars
#stars += stars
#stars += stars
#stars += stars
#stars += stars
#print(stars)
##############
keys = ['Katherine Freeman', 'Tammy Gonzalez', 'Robin Matthews', 'Sherry Farrell', 'Emma Graves', 'Tina Brown', 'George Owens', 'Ronald Ball']
values = ['katherine.freeman@hoffman.net', 'tammy.gonzalez@gomez.info', 'robin.matthews@leblanc-lyons.org', 'sherry.farrell@reynolds-johnson.net', 'emma.graves@reid-little.info', 'tina.brown@yahoo.com', 'george.owens@yahoo.com', 'ronald.ball@thomas.com']
my_dict= zip(keys, values)
my_dict = dict(my_dict)
print(my_dict)
