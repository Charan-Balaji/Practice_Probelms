def sand_clock(n):
    for i in range(n, 0, -1):
        print(" " * (n - i) + "* " * i) # printing upper triangle
        
    for i in range(2, n + 1):
        print(" " * (n - i) + "* " * i) # printing lower triangle
        
n = int(input("Enter the number of rows: ")) # getting the input from user
sand_clock(n)
