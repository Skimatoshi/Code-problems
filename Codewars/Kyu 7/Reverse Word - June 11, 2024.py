def reverse_words(text):

    reversed_string = text[::-1]
    new_list = reversed_string.split(' ')
    q = new_list[::-1]
    x = " ".join(q)

    return x

print(reverse_words('double spaces'))

# Best Practices
def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' '))