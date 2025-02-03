# perfect number
num = int(input("Enter a number: "))
sum =0
half=num//2
for i in range (1,half+1):
    if num%i==0:
        sum=sum+i
if sum==num:
    print("It is a perfect number")
else:
    print("It is Not a perfect number")