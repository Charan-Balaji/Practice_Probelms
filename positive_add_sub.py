#You have two numbers, and your challenge is to write a program that performs both addition and subtraction with them. 
# However, if any subtraction results in a negative number, display it as a positive value. How will you tackle this and show the final results?
#For example, consider two numbers 20 and 15. Addition of 2 values: 20 + 15 = 35. Subtraction of 2 values: 20 - 15 = 5. 
#For example, consider two numbers 20 and -150. Addition of 2 values: 20 + (-150) = -130 Absolute value of (-130) = 130. Subtraction of 2 values: 20 - (-150) = 170.


def calculate(a,b):
    add = a+b           # adding two numbers
    sub = a-b           # subtracting two numbers
    
    add_res = abs(add)  # abs--> absolute value, makes the negative into positive
    sub_res = abs(sub)  
    
    print(f"Addition of {a} and {b} is : {add_res}")     #printing both addition and subtraction of positive numbers
    print(f"Subtraction of {a} and {b} is : {sub_res}")
    
a = int(input("Enter the Value of A : "))               # getting user input
b = int(input("Enter the Value of B : "))
calculate(a,b)