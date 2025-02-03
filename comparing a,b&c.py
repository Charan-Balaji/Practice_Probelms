# comparing a,b and c
def sum(a,b,c):
    
    print("ALL THE POSSIBILITIES ARE:- ")
    print("1) A is Greater of all three : ",a>b and a>c)
    print("2) B is Greater of all three : ",b>a and b>c)
    print("3) C is Greater of all three : ",c>a and c>b)
    print("4) A and B are Equal         : ",a==b)
    print("5) A and C are Equal         : ",a==c)
    print("6) B and C are Equal         : ",b==c)
    print("7) A, B, c, all are Equal    : ",a==b and a==c)

a = int(input("Enter the value of A: "))
b = int(input("Enter the value of B: "))
c = int(input("Enter the value of C: "))
sum(a,b,c)