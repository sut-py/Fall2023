a, b = map(int, input().split())
start = a
end = b

if a > b:
    start = b
    end = a
count = 0

for num in range(start, end+1):
    is_prime = 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                is_prime = 0
                break
        if is_prime == 1:
            count += 1
if b >= a:
    print("main order - amount: %d" % count)
else:
    print("reverse order - amount: %d" % count)