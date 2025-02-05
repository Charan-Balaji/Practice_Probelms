#Simple interest is a quick method of calculating the interest charge on a loan. 
#Simple interest is determined by multiplying the daily interest rate by the principal by the number of days that elapse between payments. 
#Simple interest formula is given by: Simple Interest = (P x T x R)/100 
def calculate_SI(p,t,r):
    neu=p*t*r
    den=100
    SI= neu//den
    print("The Si for the given data is : ", SI)
p=int(input("Enter the Principle (in rs.) : "))
t=int(input("Enter the Time (in yrs) : "))
r=int(input("Enter the Rate of Interest (in %) : "))
calculate_SI(p,t,r)