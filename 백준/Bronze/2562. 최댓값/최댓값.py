nums = []
for _ in range(9):
    nums.append(int(input()))

max = max(nums)
print(max)

idx = nums.index(max) + 1
print(idx)
