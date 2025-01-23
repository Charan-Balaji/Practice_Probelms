#fibonacci series of 'n' terms


def fibonacci(n):                            
    
    a, b = 0, 1                              
    for _ in range(n):                        # Loop through n terms to generate the sequence
        print(a, end=" \n")                  
        a, b = b, a + b                       # Update the values of 'a' and 'b' for the next term

n = int(input("Enter the number of terms: ")) # Take input from the user for the number of terms to generate
print("Fibonacci Series for term - ",+n)    
fibonacci(n)                                  # Call the fibonacci function to print the sequence
