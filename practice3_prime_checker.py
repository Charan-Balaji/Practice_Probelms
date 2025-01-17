#check whether the given number is prime or not.

def is_prime(n):                              # Function to check if a number is prime
    
    if n <= 1:                                # If the number is less than or equal to 1, it's not prime
        return False
    
    for i in range(2, int(n ** 0.5) + 1):     # Loop from 2 to the square root of n to check for divisibility
        if n % i == 0:                        # If n is divisible by any number in this range, it's not prime
            return False
    return True                               # If no divisors are found, n is a prime number
number = int(input("Enter a number: "))       # Take input from the user for the number to check

if is_prime(number):                          # Call the is_prime function to check if the number is prime
    
    print(f"{number} is a prime number.")     # Print if the number is prime
else:
    print(f"{number} is not a prime number.") # Print if the number is not prime
