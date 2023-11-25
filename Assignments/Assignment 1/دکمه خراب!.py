n = int(input())
m = int(input())
k = int(input())
carry = 0
for _ in range(32):  
    sum_no_carry = n ^ m
    carry = (n & m) << 1
    n = sum_no_carry
    m = carry

print(n)
if n == k:
    print("YES")
else:
    print("NO")
