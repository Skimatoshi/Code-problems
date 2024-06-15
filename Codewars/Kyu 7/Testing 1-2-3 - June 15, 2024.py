def number(lines):

    my_list = []

    for index, char in enumerate(lines):
        x = index + 1
        my_list.append(str(x) + ": " + char)

    return my_list

print(number(["a", "b", "c"]))
