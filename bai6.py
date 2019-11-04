thang = int(input("nhap thang: "))
nam = int(input("nhap nam: "))
if thang == 2:
	if(nam%4 == 0 and nam/100!=0) or nam%400 == 0:
		songay = 29
		

	else:	
		songay = 28


elif thang in [1,3,5,7,8,10,12]:
	songay = 31
elif thang in [4,6,9,11]:
	songay = 30

print("so ngay :",songay)

