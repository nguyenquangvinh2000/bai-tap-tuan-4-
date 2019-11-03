print("gia tri cua x")
x = int(input())
max = 0
while x > 0:
    sodu = int(x % 10)
    x = int(x/10)
    if sodu > max:
        max = sodu

print("so lon nhat la: ",max)