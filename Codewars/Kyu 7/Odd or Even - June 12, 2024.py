def odd_or_even(arr):

    final_sum = 0

    for i in arr:
        final_sum += i

    if final_sum % 2 == 0:
        return 'even'
    else:
        return 'odd'



print(odd_or_even([0,1,-2,5,7,-4]))


# Best Practices (could have just used sum)

def oddOrEven(arr):
    return 'even' if sum(arr) % 2 == 0 else 'odd'