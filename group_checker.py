# we have three groups one group is between 40 to 50, the second group is less than 40 the third group is above 50.
# our challenge is to get a number from the user and identify groups to what the number belongs to.

def check_group(n):
    if n>40 and n<=50:                                        # providing  conditions to check for 40 to 50
        print("The Number belongs to the group : '40 to 50'")
    elif n>50:                                                # providing conditions to check for Above 50
        print("The number belongs to the group : 'ABOVE 50'")
    elif n<40:                                                # providing conditions to check for Below 40 
        print("The number belongs to the group : 'BELOW 40'")
    else:                                                     # if the number does not matches it prints INVALID
        print("Invalid number")
n = int(input("Enter a number to check Group : "))            # getting input from the user
check_group(n)                                                # calling our function to check the groups
