def is_triangle_numbers(s):
    sum = 0
    for x in range(s.__len__()):
        sum += ord(s[x]) - 64
    check = 0;
    n = 1
    while check <= sum:
        check = (n * (n + 1)) / 2
        n += 1
        if check == sum:
            break
    if check == sum:
        return s + " is triangle word"
    else:
        return s + " is not triangle word"

print(is_triangle_numbers("SKY"))