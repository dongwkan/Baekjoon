def num(c):
    if ord(c) >= ord('A'):
        rst = ord(c) - ord('A') + 10
        return rst
    else:
        return int(c)

N, B = input().split()
B = int(B)
ver_10 = 0

for i in range(len(N)):
    p = num(N[- (i + 1)]) * (B ** i)
    ver_10 += p

print(ver_10)
