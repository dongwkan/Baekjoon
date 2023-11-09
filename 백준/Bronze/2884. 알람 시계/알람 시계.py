H, M = map(int, input().split())

setTime = (H * 60 + M - 45)
if setTime < 0:
    setTime = (24 * 60 + M - 45)
    
setTime_H = setTime // 60
setTime_M = setTime % 60

print(str(setTime_H) + " " + str(setTime_M))
