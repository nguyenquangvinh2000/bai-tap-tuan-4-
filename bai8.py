n=int(input("n="))

m=n
s=int(0)
while n > 0:
  a= int(n % 10)
  s=int(s*10+a)
  n=int(n/10)

if m==s:
  print("đây là số đối xứng")
else:
  print("đây không phải là số đối xứng")