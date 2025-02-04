# gcd calculator program
def gcd_calculator(a, b):
    while b:
        a, b = b, a % b  # calculating GCD for the two programs
    return a

a = int(input("Enter Number 1 : ")) # getting input from the user
b = int(input("Enter Number 2 : "))

print(f"GCD of {a} and {b} is {gcd_calculator(a, b)}") # printing the calculated GCD using f string

