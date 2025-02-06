# program to check if the year is leap or not
def check_leap():
    if(yr%400==0):                         # for years that leaves 0 on dividing by 400   
        print("It is a Leap Year")    
    elif(yr%100==0):                       # other conditions to check for century 
        print("It is Not a Leap Year")        
    elif(yr%4==0):                         # for years that leaves 0 on dividing by 4
        print("It is a Leap Year")
    else:
        print("It is Not a Leap Year")
    
yr=int(input("Enter Year to Check : "))    # getting input from user
check_leap()                               # calling the function that we've created 
