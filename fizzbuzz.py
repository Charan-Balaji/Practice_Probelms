#%3 fizz, %5 buzz, %3 and %5 fizzbuzz, no --> num alone
def fb(n):
    if(n%3==0):
        print("FIZZ")
    elif(n%5==0):
        print("BUZZ")
    elif(n%3==0 and n%5==0):
        print("FIZZBUZZ")
    else:
        print("It was not matching with any number ---> ",n)

n = int(input("Enter a Number: "))
fb(n)