#find the sum of 'n' natural numbers
def sum_of_natural_numbers(n): # Function to calculate the sum of natural numbers up to 'n'
    return n * (n + 1) // 2    # Formula to calculate the sum of natural numbers

number = int(input("Enter a number: "))  # Taking user input for the number
print(f"The sum of the first {number} natural numbers is: {sum_of_natural_numbers(number)}.")  # Output the sum
