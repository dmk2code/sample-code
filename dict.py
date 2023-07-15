x = [("A", 65), ("B", 66), ("C", 67), ("D", 68)]
keys = []
values = []
for d in x:
    keys.append(d[0])
    values.append(d[1])
    c = zip(keys, values)
    dic = dict(c)
print (dic)