# Imagine you need to repeat a cheerful message. Write a program that uses a for loop to print "ALL IS WELL" exactly twenty times. 
# How will you set up your loop to ensure this message appears the right number of times?

def repeat_message():
    for _ in range(20):  # we use for loop to loop from 0 to 19 that 20 times
        print("ALL IS WELL")
print("Printing Message exactly 20 times \n")
repeat_message()
