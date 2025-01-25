#check whether the given number is an armstrong  number or not
def is_armstrong(n):                                                  # Function to check if a number is Armstrong
    digits = str(n)                                                   # Convert the number to a string to easily iterate over digits
    num_digits = len(digits)                                          # Find the number of digits in the number
    sum_of_powers = sum(int(digit) ** num_digits for digit in digits) # Calculate the sum of digits raised to the power of num_digits
    return sum_of_powers == n                                         # Return True if the sum equals the original number, else False

number = int(input("Enter a number: "))                               # Taking user input for number
if is_armstrong(number):                                              # Check if the number is Armstrong
    print(f"{number} is an Armstrong number.")                        # Output Armstrong number message
else:                                                                 # If the number is not Armstrong
    print(f"{number} is not an Armstrong number.")                    # Output non-Armstrong message
