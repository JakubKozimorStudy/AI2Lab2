def is_cyclone_phrase(s):
    len = s.__len__()
    front = 0
    back = -1
    tab = []
    for x in range(len):
        if x % 2 == 0:
            if s[front] != " ":
                tab.append(s[front])
            front += 1
        else:
            if s[back] != " ":
                tab.append(s[back])
            back -= 1

    tabSort = sorted(tab)
    if(tabSort == tab ):
        return "is_cyclone_phrase('" +s+"') # => True"
    else:
        return "is_cyclone_phrase('" +s+"') # => False"

print(is_cyclone_phrase("a  bcb a"))
print(is_cyclone_phrase("adjourned"))
print(is_cyclone_phrase("settled"))