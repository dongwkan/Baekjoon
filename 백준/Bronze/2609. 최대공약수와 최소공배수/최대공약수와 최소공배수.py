A, B = map(int, input().split())
C = min(A, B)

while True:
    if A % C == 0 and B % C == 0:
        GCD = C
        break
    C -= 1

a = A // GCD
b = B // GCD
LCM = a * b * GCD

print(GCD)
print(LCM)
