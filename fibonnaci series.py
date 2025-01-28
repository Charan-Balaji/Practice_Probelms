def fib(n):
    n1 = 0             # initializing n1 variable with 0
    n2 = 1             # initializing n2 variable with 1
    print(n1)
    print(n2)
    for i in range(n): # perform iteration so that the series continues until condition fails 
        n3 = n2+n1     # adding n1 and n2 
        print(n3)
        n1 = n2        # swapping values of n2 to n1
        n2 = n3        # swapping values of n3 to n2
        
        
n = int(input("Enter a Number : "))
fib(n)                # calling fib function