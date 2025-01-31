# hollow square pattern with "*"

def hollow_square(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1: # we have to print * for the border and space inside
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()  # Move to the next line after each row printing

size = int(input("Enter the size of square: ")) # getting the input from the user, as the size of square
hollow_square(size)  # calling our function and passing the input size as argument
