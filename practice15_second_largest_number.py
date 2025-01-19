#program that finds the second largest number in a list
def second_largest(lst):                       # Function to find the second largest element in the list
    if len(lst) < 2:                           # If the list has less than two elements, return None
        return None
    largest = second = float('-inf')           # Initialize largest and second with negative infinity
    for num in lst:                            # Loop through each element in the list
        if num > largest:                      # If the current number is greater than largest
            second = largest                   # Update second to be the old largest
            largest = num                      # Update largest to the current number
        elif num > second and num != largest:  # If current number is less than largest but greater than second
            second = num                       # Update second
    return second                              # Return the second largest element

lst = list(map(int, input("Enter elements separated by space: ").split()))  # Taking user input for the list
print(f"The second largest element in the list is: {second_largest(lst)}")  # Output the second largest element
