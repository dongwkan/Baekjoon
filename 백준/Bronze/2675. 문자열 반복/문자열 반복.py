T = int(input())

for _ in range(T):
    R, S = input().split()
    R = int(R)
    for c in S:
        for _ in range(R):
            print(c, end = "")
    print("")
