T = int(input())
for i in range(T):
    A, B = [int(x) for x in input().split()]
    print("Case #" + str(i + 1) + ": "
          + str(A) + " + " + str(B) + " = " + str(A + B))
