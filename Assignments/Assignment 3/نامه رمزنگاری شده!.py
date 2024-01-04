string = input()
words = string.split(' ')

answer = [None] * len(words)

def print_from_array(answer):
    print(''.join(answer))

for w in words:
    c = w[0]
    i = int(w[1:])
    answer[i] = c

print_from_array(answer)