def generate_pascal_row(s):
    len = s.__len__()
    tab = []
    for x in range(len+1):
        if x == 0 or x == len:
            tab.append(1)
        else:
            tab.append(s[x-1] + s[x])
    return tab

print(generate_pascal_row([]))
print(generate_pascal_row([1, 2, 1]))
print(generate_pascal_row([1, 4, 6, 4, 1]))