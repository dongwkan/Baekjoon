score = int(input())

if score >= 90:
    rst = "A"
elif score >= 80:
    rst = "B"
elif score >= 70:
    rst = "C"
elif score >= 60:
    rst = "D"
else:
    rst = "F"

print(rst)
