a = int(input("nhập ngày: "))
b = int(input("nhập tháng: "))
c = int(input("nhập năm: "))

if a == 31:
    if b in [1,3,5,7,8,10]:
        print(1,b+1,c)
    elif b == 12:
        print(1,1,c+1)

elif a == 30:
    if b in [2,4,6,9,11]:
        print(1,b+1,c)
elif a < 30:
    print(a+1,b,c)
elif a in [30,31] and b == 2:
    print("không tồn tại")
