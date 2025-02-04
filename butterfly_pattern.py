# program that prints butterfly pattern '*'

def butterfly_pattern(n):
    for i in range(1, n + 1):  #  '*' to build upper right triangle and " " to make spaces
        print("*" * i + " " * (2 * (n - i)) + "*" * i)   
    for i in range(n - 1, 0, -1):  #  '*' to build lower right triangle and " " to make spaces
        print("*" * i + " " * (2 * (n - i)) + "*" * i)  

n = int(input("Enter the number of rows: "))  # getting input number of rows
butterfly_pattern(n)
