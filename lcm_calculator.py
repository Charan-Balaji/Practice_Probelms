# lcm calculator programs
def gcd(a, b):
    while b:
        a, b = b, a % b # calculating GCD which will be useful 
    return a 

def lcm(a, b):
    return (a * b) // gcd(a, b) # calculating LCM using the GCD

a = int(input("Enter Number 1 : ")) # getting the input from the user
b = int(input("Enter Number 2 : "))

print(f"LCM of {a} and {b} is {lcm(a, b)}") # printing  lcm that we calculated 
