#program to find the largest number in the given list 
def largest_element(lst):  # Function to find the largest element in the list
    largest = lst[0]       # Assume the first element is the largest
    for num in lst:        # Loop through each number in the list
        if num > largest:  # If the current number is larger than the assumed largest
            largest = num  # Update the largest element
    return largest         # Return the largest element

numbers = list(map(int, input("Enter numbers separated by space: ").split())) # Taking user input for numbers
print(f"The largest number in the list is: {largest_element(numbers)}.")      # Output the largest number
