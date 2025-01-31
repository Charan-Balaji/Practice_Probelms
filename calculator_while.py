#You‟re tasked with creating a simple calculator using a while loop and a switch statement. Your program should repeatedly prompt the user to choose an arithmetic operation
#like addition, subtraction, multiplication, or division) and then perform the selected operation based on user input. How will you set up your while loop and 
# switch case to keep the calculator running until the user decides to exit.

def calculator():  # defining the function that will execute the actual logic
    while True:    
        menu = """\nSimple Calculator
        1. Addition (+)
        2. Subtraction (-)
        3. Multiplication (*)
        4. Division (/)
        5. Exit
        Enter your choice (1-5): """  # printing the menu that as the list of operations, using ''' to make multiple lined comments.
        
        choice = input(menu) # printing the menu
        
        if choice == '5':   # exiting the loop if the user's have to option to exit the program
            print("Exiting the calculator. Goodbye!")
            break  
        
        if choice not in ('1', '2', '3', '4'):
            print("Invalid input! Please enter a number between 1 and 5.")
            continue  # Skip the rest and ask again, using continue
        
        num1 = float(input("Enter first number: "))  # getting the input from the user
        num2 = float(input("Enter second number: "))
        print("---   ---   ---   ---   ---")
        
        match choice:  #using match case to perform switch case in python
            case '1': # performs addition
                result = num1 + num2
                print(f"Result: {num1} + {num2} = {result}")
            case '2': # performs subtraction
                result = num1 - num2
                print(f"Result: {num1} - {num2} = {result}")
            case '3': # performs multiplication
                result = num1 * num2
                print(f"Result: {num1} * {num2} = {result}")
            case '4':# performs division (if num2 is zero, than it will not allow to run)
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    result = num1 / num2
                    print(f"Result: {num1} / {num2} = {result}")

calculator()
