T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    Y = N % H
    X = N // H + 1
    if Y == 0:
        Y = H
        X = N // H
        
    if X >= 10:
        print(str(Y) + str(X))
    else:
        print(str(Y) + "0" + str(X))
