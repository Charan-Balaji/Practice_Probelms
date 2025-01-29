# Write a program to check the given number is divisible by both 3 and 4 if it is so print "Good morning". 
# If the number is divisible by only 4, but not by 3 then print "Good afternoon". if it is divisible by only 3 and not by 4, then "Good evening". otherwise, "Good night".

# Write a program to check the given number is divisible by both 3 and 4 if it is so print "Good morning". 
# If the number is divisible by only 4, but not by 3 then print "Good afternoon". if it is divisible by only 3 and not by 4, then "Good evening". otherwise, "Good night".

def check_divisibility(number): 
    if number % 3 == 0 and number % 4 == 0:        # providing the necessary conditions given in the statement 
        print("Good morning")
    elif number % 4 == 0:
        print("Good afternoon")
    elif number % 3 == 0:
        print("Good evening")
    else:
        print("Good night")


num = int(input("Enter a number: "))              # getting input from the user
check_divisibility(num)                           # calling our function to check verify and execute the correct statement

