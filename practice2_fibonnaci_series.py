#fibonacci series of 'n' terms


def fibonacci(n):                             # Function to generate the Fibonacci sequence up to n terms
    
    a, b = 0, 1                               # Initialize the first two terms of the sequence, a=0 and b=1
    for _ in range(n):                        # Loop through n terms to generate the sequence
        print(a, end=" \n")                   # Print the current value of 'a' followed by a space
        a, b = b, a + b                       # Update the values of 'a' and 'b' for the next term

n = int(input("Enter the number of terms: ")) # Take input from the user for the number of terms to generate
print(f"Fibonacci Series for {n} terms\n")    # Print the series name as fibonacci series
fibonacci(n)                                  # Call the fibonacci function to print the sequence