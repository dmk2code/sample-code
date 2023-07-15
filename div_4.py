in_put = ["adilakshmi","venkanna","sairam","manikanta","swagatika","dmk","kushi","mama","janu","hp"]
out = []
for x in in_put:
    if len(x)//4!=0:
        out.append(x)
print(out)