X = int(input())
up = 1
down = 1

for _ in range(X - 1):
    if up == 1 and down % 2 == 1:
        down += 1
    elif up % 2 == 0 and down == 1:
        up += 1
    elif (up + down) % 2 == 1:
        up += 1
        down -= 1
    else:
        up -= 1
        down += 1

print(str(up) + "/" + str(down))
