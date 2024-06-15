def digitize(n):
    if n == 0:
        return [0]

    else:
        new_list = []
        x = list(str(n))

        for i in x:
            if type(i) == str:
                new_list.append(int(i))

        return new_list[::-1]


print(digitize(12345))

# Best Practices
def digitize(n):
    return [int(x) for x in str(n)[::-1]]