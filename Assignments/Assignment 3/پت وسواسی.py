line = input().split()
fixSpaces = " ".join(line)

lineCharacters = list(fixSpaces)
sharp_cnt, at_cnt = 0, 0

tmp = []
prev_char = ""

for c in lineCharacters:
    tmp.append(c)
    if c == '@':
        at_cnt += 1
    elif c == '#':
        if at_cnt > sharp_cnt:
            sharp_cnt += 1
            tmp.pop()
    elif c == 'n':
        if prev_char == '\\':
            tmp.pop()
            tmp.pop()
            tmp += "\n"
    prev_char = c

result = "Formatted Text: "

for c in tmp:
    result += c

print(result.strip())