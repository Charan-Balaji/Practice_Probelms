# create a basic multiplication table
def multiplication_table(n):           # Function to generate a multiplication table for 'n'
    for i in range(1, 11):             # Loop through numbers 1 to 10
        print(f"{n} x {i} = {n * i}")  # Print the multiplication of 'n' with 'i'

number = int(input("Enter a number to generate its multiplication table: "))  # Taking input for number
multiplication_table(number)  # Call the function to print the table
