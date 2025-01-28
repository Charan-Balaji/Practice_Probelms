# A washing machine works on the principle of Fuzzy System, the weight of clothes put inside it for washing is uncertain but based on weight measured by sensors 
#and the water level chosen, it decides total time needed. 
#For low level water, the time estimate is 25 minutes, where approximately weight is between 2000 grams or any nonzero positive number below that.
#For medium level water, the time estimate is 35 minutes, where approximately weight is between 2001 grams and 4000 grams.
#For high level water, the time estimate is 45 minutes, where approximately weight is above 4000 grams. Assume the capacity of machine is maximum 7000 grams. 
#When the weight is zero, time needed is 0 minutes. 
#If the weight exceeds maximum weight limit, then, print “OVERLOADED”, and for all negative weights, the output is “INVALID INPUT”.
#Sample Input-1: 2000, L
#Sample Output-1: Time Estimated: 25 minutes
#Input should be in the form of integer value. 
#Output must have the following format: Time Estimated: NN Minutes

def washing_machine(weight, water_level):
    if weight < 0:                                        # defining all  the conditions given in the question
        print("INVALID INPUT!!!")
    elif weight == 0:
        print("Estimated Time : 0 Minutes")
    elif weight > 7000:
        print("OVERLOADED!!")
    else:  
        if water_level == 'L' and 0 < weight <= 2000:
            print("Estimated Time : 25 Minutes")
        elif water_level == 'M' and 2001 <= weight <= 4000:
            print("Estimated Time : 35 Minutes")
        elif water_level == 'H' and weight > 4000:
            print("Estimated Time : 45 Minutes")
        else:
            print("INVALID!!")                              # If the water level does not match conditions

weight = int(input("Enter weight of clothes in grams: "))   # Taking weight input from the user
water_level = input("Enter water level (L/M/H): ").upper()  # changing to upper case, because i'm using upper case in the conditions

washing_machine(weight, water_level)                        # Calling the function

    