#find the sum of a given number

def sum_of_digits(n):                                                
    total = 0                                                      
    while n > 0:                                                     # Loop until the number becomes 0
        total += n % 10                                              # Add the last digit of the number to the total
        n = n // 10                                                  # Remove the last digit from the number
    return total                                                     # Return the final sum of digits

number = int(input("Enter a number: "))                             
print("The sum of digits of" ,number "is", sum_of_digits(number)) 
