def sum_mix(arr):
    
    sum = 0

    for i in arr:
        if type(i) == str:
            sum += int(i)
        else:
            sum += i

    return sum





print(sum_mix([1, 3, '4', '5']))

# Hint
# Variable that starts with 0
