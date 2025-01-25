#find the prime numbers in a given range 
def find_primes(start, end):                      
    primes = []                                      # List to store prime numbers
    for num in range(start, end):                
        if num > 1:                                  # A prime number is greater than 1
            for i in range(2, int(num ** 0.5) + 1):  # Check divisibility from 2 to square root of num
                if num % i == 0:                     # If num is divisible by any number, it's not prime
                    break                            
            else:                                   
                primes.append(num)                  
    return primes                                    # Return the list of prime numbers

start = int(input("Enter the start of the range: ")) # Taking user input 
end = int(input("Enter the end of the range: "))    
print("Prime numbers between the given range is : " find_primes(start, end))  # Output the list of primes
