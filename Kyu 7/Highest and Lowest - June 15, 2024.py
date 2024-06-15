def high_and_low(numbers):
    joined = numbers.strip()
    new_list = joined.split(" ")
    main_list = [int(i) for i in new_list]



    x = min(main_list)
    q = max(main_list)

    return f'{str(q)} {str(x)}'



print(high_and_low(' 1 2 3 -4 5 '))

# Best Practices

def high_and_low(numbers):
  numbers = [int(c) for c in numbers.split(' ')]
  return f"{max(numbers)} {min(numbers)}"