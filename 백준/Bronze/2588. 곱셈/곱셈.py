A = int(input())
B = int(input())
B_100 = B // 100
B_10 = (B % 100) // 10
B_1 = (B % 100) % 10

print(A * B_1)
print(A * B_10)
print(A * B_100)
print(A * B)
