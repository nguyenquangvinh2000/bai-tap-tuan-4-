year = int(input("year="))
def checkyear (year):



    return (((year%4==0) and (year % 100 != 0)) or (year % 400 == 0))
if (checkyear(year)):
    print("năm nhuận")
else:
    print("không phải năm nhuận")
