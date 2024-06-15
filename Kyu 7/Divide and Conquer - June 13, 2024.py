def div_con(x):

    non_integers = 0
    string_integers = 0

    for i in x:
        if type(i) == str:
            non_integers += int(i)
        else:
            string_integers += i


    return string_integers - non_integers




print(div_con([9, 3, '7', '3']))
