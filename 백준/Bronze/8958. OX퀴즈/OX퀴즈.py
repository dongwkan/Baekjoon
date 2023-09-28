N = int(input())
for _ in range(N):
    cnt = 0
    cnts = []
    case = input()
    for c in case:
        if c == "O":
            cnt += 1
            cnts.append(cnt)
        else:
            cnt = 0
            cnts.append(cnt)
    score = sum(cnts)
    print(score)
