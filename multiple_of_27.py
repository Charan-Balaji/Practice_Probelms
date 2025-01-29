# You have a number to examine, and your mission is to write a program that checks whether this number can be divided evenly by 27. 
# Can you find out if it‟s a multiple of 27?

def multiple_27(number):
    if number % 27 == 0:
        print("It is a Multiple of 27.")
    else:
        print("It is NOT a Multiple of 27.")

num = int(input("Enter a number: "))
multiple_27(num)
