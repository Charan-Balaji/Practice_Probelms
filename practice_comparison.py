# You have two secret numbers, and you need to figure out how they relate to each other using a set of special tools. 
# Your challenge is to write a program that uses these tools—>, >=, <, <=, ==, and !=—to uncover all the secrets 
# about how these numbers compare. How will you use each tool to solve the puzzle?

def compare():                         # This function will compare and print the secrets 
    print(n1, "<", n2, "=", n1 < n2)          
    print(n1, "<=", n2, "=", n1 <= n2)
    print(n1, ">", n2, "=", n1 > n2)
    print(n1, ">=", n2, "=", n1 >= n2)
    print(n1, "==", n2, "=", n1 == n2)
    print(n1, "!=", n2, "=", n1 != n2)
    
n1 = int(input("Enter number N1: "))    # Getting inputs from the user
n2 = int(input("Enter number N2: "))

print("Revealing the Comparison of these numbers\n") 
compare()                               # calling sour function
