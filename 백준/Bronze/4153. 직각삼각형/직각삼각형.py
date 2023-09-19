while True:
    A, B, C = sorted(list(map(int, input().split())))
    if A == B == C == 0:
        break
    if C ** 2 == A ** 2 + B ** 2:
        print("right")
    else:
        print("wrong")
