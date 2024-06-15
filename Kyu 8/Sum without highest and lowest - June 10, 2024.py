def sum_array(arr):

    if arr == None:
        return 0

    if len(arr) <= 2:
        return 0

    else:
        arr.remove(max(arr))
        arr.remove(min(arr))
        return sum(arr)

print(sum_array([None]))

# Best Practices

def sum_array(arr):
    if arr == None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)
