#Given dictionary representing a student name as a key and corresponding value is a grade
# which he obtained in different subjects.  WAP update each dict value with average score
# obtained by each student respectively.
def score(scores):
    scr = {}
    k = []
    input_range = int(input("enter the range of element:"))
    for x in range(input_range):
        keys = input("enter the keys: ")
        v = []
        for y in range(input_range):
            a = input("enter the values: ")
            v.append(a)
        scr[keys] = v
    add = []
    join = []
    a1 = []
    a2 = []
    a3 = []
    a4 = []
    b = 0
    c = 0
    d = 0
    e = 0
    for x in scr.keys():
        join.append(x)
    for y in scr.values():
        add.append(y)
    a1.append(add[0])
    a2.append(add[1])
    a3.append(add[2])
    a4.append(add[3])
    for d1 in a1:
        for z1 in d1:
            b += z1
    b = b / len(y)
    for d2 in a2:
        for z2 in d2:
            c += z2
    c = c / len(y)
    for d3 in a3:
        for z3 in d3:
            d += z3
    d = d / len(y)
    for d4 in a4:
        for z4 in d4:
            e += z4
    e = e / len(y)

    total = [b, c, d, e]

    res = {join[i]: total[i] for i in range(len(join))}
    print(res)


score([])