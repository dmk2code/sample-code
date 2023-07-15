lis_t = ["karma", "mama", "kungfu", "cricket"]
reverse =lis_t[0][::-1], lis_t[1][::-1], lis_t[2][::-1], lis_t[3][::-1]
re_reverse = []
for x in reverse:
    re_reverse.append(x)
print(re_reverse[::-1])