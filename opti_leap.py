# optimized leap year program
def check_leap():
    yr=int(input("Enter any Year : "))
    if(yr%4==0)&(yr%100!=0)|(yr%400==0):  # using single if statement, we verify all three conditions
        print("It is a Leap Year")
    else:
        print("It is NOt a Leap Year")
check_leap()     