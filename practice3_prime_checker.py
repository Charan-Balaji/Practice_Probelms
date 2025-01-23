#check whether the given number is prime or not.

def is_prime(n):                              
    
    if n <= 1:                              
        return False
    
    for i in range(2, int(n ** 0.5) + 1):     # Loop from 2 to the square root of n to check for divisibility
        if n % i == 0:                        # If n is divisible by any number in this range, it's not prime
            return False
    return True                               # If no divisors are found, n is a prime number
number = int(input("Enter a number: "))       

if is_prime(number):                          # Call the is_prime function to check if the number is prime
    
    print("It is a prime number.")   
else:
    print("It is not a prime number.") 
