#find the prime numbers in a given range 
def find_primes(start, end):                         # Function to find all prime numbers in a given range
    primes = []                                      # List to store prime numbers
    for num in range(start, end + 1):                # Loop through the range from 'start' to 'end'
        if num > 1:                                  # A prime number is greater than 1
            for i in range(2, int(num ** 0.5) + 1):  # Check divisibility from 2 to square root of num
                if num % i == 0:                     # If num is divisible by any number, it's not prime
                    break                            #break to exit the loop
            else:                                    # If no divisor found, the number is prime
                primes.append(num)                   # call the function
    return primes                                    # Return the list of prime numbers

start = int(input("Enter the start of the range: ")) # Taking user input for start
end = int(input("Enter the end of the range: "))     # Taking user input for end
print(f"Prime numbers between {start} and {end}: {find_primes(start, end)}.")  # Output the list of primes
