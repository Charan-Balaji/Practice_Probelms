# greatest and smallest of two numbers
def num_check(n1,n2):
    if n1<n2:                            # checking conditions for greater and smaller number
        print(f"The Greatest Number is : {n2} \nThe Smallest Number is : {n1}")
    elif n2<n1:
        print(f"The Greatest Number is : {n1} \nThe Smallest Number is : {n2}")
    else:
        print("Both Numbers are Equal")
n1 = int(input("Enter the Number N1: ")) # getting inputs of n1 and n2 from the user
n2 = int(input("Enter the Number N1: "))
num_check(n1,n2)                         # calling the function that we've created