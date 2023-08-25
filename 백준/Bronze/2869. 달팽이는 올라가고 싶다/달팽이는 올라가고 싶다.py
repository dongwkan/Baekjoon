A, B, V = [int(x) for x in input().split()]

if (V - A) % (A - B) == 0:
    day = (V - A) // (A - B) + 1
else:
    day = (V - A) // (A - B) + 2

print(day)


