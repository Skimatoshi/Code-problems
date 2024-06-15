string = 'helloo'

answer = []

for i in range(0,len(string), 2):
    answer.append(string[i] + string[i + 1])


print(answer)