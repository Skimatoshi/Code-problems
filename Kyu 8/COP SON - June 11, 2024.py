def count_positives_sum_negatives(arr):
    positive_list = []
    negative_list = []
    final_list = []

    if arr == []:
        return []

    for i in arr:
        if i >= 1:
            positive_list.append(i)

        elif i < 1:
            negative_list.append(i)

    x = len(positive_list)
    q = sum(negative_list)

    final_list.append(x)
    final_list.append(q)

    return final_list


print(count_positives_sum_negatives([]))

# Best Practices

def count_positives_sum_negatives(arr):
    if not arr: return []
    pos = 0
    neg = 0
    for x in arr:
      if x > 0:
          pos += 1
      if x < 0:
          neg += x
    return [pos, neg]
