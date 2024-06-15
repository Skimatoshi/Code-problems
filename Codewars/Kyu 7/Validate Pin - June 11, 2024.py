def validate_pin(pin):


    new_list = list(pin)

    real_list = []

    for i in new_list:
        if i.isdigit():
            real_list.append(i)
        else:
            return False

    if len(real_list) in (4,6):
        return True
    else:
        return False




print(validate_pin('22.33'))

# Best practices

def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()