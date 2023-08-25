N, M = [int(x) for x in input().split()]
A = []
B = []
C = []

for i in range(N):
    A.append([int(y) for y in input().split()])
for j in range(N):
    B.append([int(z) for z in input().split()])

for row in range(N):
    for col in range(M):
        C.append(A[row][col] + B[row][col])
    for item in C:
        print(item, end = " ")
    print("")
    C = []
