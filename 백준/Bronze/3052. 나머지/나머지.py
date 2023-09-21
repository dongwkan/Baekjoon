nums = []

for _ in range(10):
    a = int(input()) % 42
    nums.append(a)

rst = len(set(nums))
print(rst)
