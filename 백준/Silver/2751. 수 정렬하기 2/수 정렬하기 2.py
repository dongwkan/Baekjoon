N = int(input())
nums = []

for _ in range(N):
    nums.append(int(input()))

nums = sorted(nums)

for item in nums:
    print(item)
