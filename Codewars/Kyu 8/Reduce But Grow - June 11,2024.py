def grow(arr):
    final_sum = 1

    for i in arr:
        final_sum *= i

    return final_sum





print(grow([1,2,3]))
