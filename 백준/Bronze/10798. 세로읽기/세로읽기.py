words = []
rst = []
max_len = 0

for i in range(5):
    words.append(input())

for j in words:
    if len(j) > max_len:
        max_len = len(j)

for k1 in range(max_len):
    for k2 in range(5):
        if k1 <= len(words[k2]) - 1:
            c = words[k2][k1]
            rst.append(c)
        
for item in rst:
    print(item, end = "")
