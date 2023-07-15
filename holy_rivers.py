holy_rivers = ["Ganges", "Godavari", "Bramhaputra", "Narmada", "yemuna", "Mahanadi", "Kaveri", "Tapati"]
rivers = []
for holy in range(len(holy_rivers)):
    x = str(holy)
    x = ord(x)
    rivers.append(x)
print(rivers)