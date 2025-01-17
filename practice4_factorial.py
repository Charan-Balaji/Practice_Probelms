#find the factorial of 'n' number.

def factorial(n):  # Function to calculate the factorial using recursion
    if n == 0 or n == 1:  # Base case: if n is 0 or 1, return 1
        return 1
    return n * factorial(n - 1)  # Recursive case: n multiplied by factorial of (n-1)

number = int(input("Enter a number: "))  # Take input from the user
print(f"The factorial of {number} is {factorial(number)}.")  # Print the result of the factorial calculation
