#find the factorial of 'n' number.

def factorial(n):  
    if n == 0 or n == 1:  #if n is 0 or 1, we are returning 1
        return 1
    return n * factorial(n - 1)  # n multiplied by factorial of (n-1)

number = int(input("Enter a number: "))  
print("The factorial of", number, "is", factorial(number))   # Print the result of the factorial
