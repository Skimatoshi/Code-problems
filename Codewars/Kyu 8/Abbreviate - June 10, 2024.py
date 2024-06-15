def abbrev_name(name):
    
    x,q = name.split(' ')
    return x[0].upper() + "." + q[0].upper()

print(abbrev_name('Justin Wu'))