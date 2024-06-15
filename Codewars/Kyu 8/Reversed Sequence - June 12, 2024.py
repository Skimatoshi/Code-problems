def reverse_seq(n):

    # new = []
    #
    # for i in range(1, n+1):
    #     new.append(i)
    #
    # return new[::-1]

    return [i for i in range(n, 0, -1)]

print(reverse_seq(5))