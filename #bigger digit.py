#bigger digit
num = int(input("Enter a number: "))
big = 0  
temp = num  

while temp > 0:
    digit = temp % 10  
    if digit > big:
        big = digit  
    temp = temp // 10  

print("The largest digit is:", big)
