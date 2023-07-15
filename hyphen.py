str1 = "PYTHON"
str2 = range(len(str1)-1)
str3 = []
for x in str2:
    x='-'
    str3.append(x)
str4 = str1[0]+" "+str3[0],str1[1]+" "+str3[1],str1[2]+" "+str3[2],str1[3]+" "+str3[3],str1[4]+" "+str3[4],str1[5]
print(*str4)

