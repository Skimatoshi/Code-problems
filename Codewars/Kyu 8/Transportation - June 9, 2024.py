# My solution

def rental_car_cost(d):
    if d < 3:
        d *= 40
        return d
    elif 3 <= d <= 6:
        d = d * 40 - 20
        return d
    elif d >= 7:
        d = d * 40 - 50
        return d

# Best practices

def rental_car_cost(d):
    result = d * 40
    if d >= 7:
        result -= 50
    elif d >= 3:
        result -= 20
    return result