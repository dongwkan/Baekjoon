N, X = map(int, input().split())
A = list(map(int, input().split()))
rst = []

for i in A:
    if i < X:
        rst.append(i)

for j in rst:
    print(j, end=" ")
print()
