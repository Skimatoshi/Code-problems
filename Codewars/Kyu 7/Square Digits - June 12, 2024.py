def square_digits(num):

    x = str(num)
    q = list(x)

    new_list = []
    str_list = []


    for i in q:
        change_int = int(i)
        new_list.append(change_int ** 2)

    for i in new_list:
        str_list.append(str(i))

    final_str = "".join(str_list)

    return int(final_str)


print(square_digits(9119))

# Best Practices

def square_digits(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)