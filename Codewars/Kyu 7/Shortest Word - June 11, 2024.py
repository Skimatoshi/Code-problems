def find_short(s):
    new_list = []

    x = s.split(' ')

    for i in x:
        new_list.append(len(i))

    return min(new_list)

# Best practice

def find_short(s):
    return min(len(x) for x in s.split())