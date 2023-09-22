nums = list(map(int, input().split()))
rst = 0

for i in nums:
    rst += (i ** 2)

rst = rst % 10

print(rst)
