N = int(input())
nums = list(map(int, input().split()))
cnt = 0
rst = 0

for i in nums:
    if i != 1:
        for j in range(1, i + 1):
            if i % j == 0:
                cnt += 1
        if cnt == 2:
            rst += 1
    cnt = 0

print(rst)
