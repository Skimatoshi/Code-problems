def word_search(query, seq):

    new_list = []



    for i in seq:
        if query.lower() in i.lower():
            new_list.append(i)


    if len(new_list) == 0:
        return ['None']
    if seq == []:
        return ['None']


    return new_list

print(word_search('aB', ["za", "ab", "abc", "zab", "zbc"]))

# Was helped a lot by KraziKiwi, but nonetheless I did it
# Best Practices
def word_search(query, seq):
    return [x for x in seq if query.lower() in x.lower()] or ["None"]