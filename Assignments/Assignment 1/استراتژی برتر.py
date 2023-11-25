a = int(input())
b = int(input())
c = a ^ b

bit = 1

counter = 0

for i in range(31):
    if bit & c == bit:
        counter += 1
    bit = bit << 1
    
print(counter)