print("gia tri cua x")
x = int(input())
max = 0
while x > 0:
    y = int(x % 10)
    x = int(x/10)
    if y > max:
        max = y

print(max)
