num1 = int(input())
num2 = int(input())
n = int(input())

for i in range(n):
    x = int(input())
    p = num1 & (1 << x) if x < 32 else num2 & (1 << (x - 32))
    print("yes" if p != 0 else "no")
