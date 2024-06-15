def filter_list(l):
    real_list = []
    for i in l:
        if type(i) == int:
            real_list.append(i)

    return real_list

filter_list([1,2,'hello'])

# Received help from Gray, hint : using type() to check whether it is string
# or not