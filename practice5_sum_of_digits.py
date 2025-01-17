#find the sum of a given number

def sum_of_digits(n):                                                # Function to calculate the sum of digits of the number
    total = 0                                                        # Variable to store the sum of digits
    while n > 0:                                                     # Loop until the number becomes 0
        total += n % 10                                              # Add the last digit of the number to the total
        n = n // 10                                                  # Remove the last digit from the number
    return total                                                     # Return the final sum of digits

number = int(input("Enter a number: "))                              # Take input from the user
print(f"The sum of digits of {number} is {sum_of_digits(number)}.")  # Print the sum of digits of the entered number
