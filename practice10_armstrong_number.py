#check whether the given number is an armstrong  number or not
def is_armstrong(n):                                                  
    digits = str(n)                                                   # Convert the number to a string to easily iterate over digits
    num_digits = len(digits)                                          # Find the number of digits in the number
    sum_of_powers = sum(int(digit) ** num_digits for digit in digits) # Calculate the sum of digits raised to the power of num_digits
    return sum_of_powers == n                                        

number = int(input("Enter a number: "))                               
if is_armstrong(number):                                              # Check if the number is Armstrong
    print("It is an Armstrong number.")                        
else:                                                                
    print("It is not an Armstrong number.")                    
