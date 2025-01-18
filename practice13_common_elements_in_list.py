#finding the common elements between two given list 
def common_elements(list1, list2):                                                              # Function to find common elements between two lists
    return [element for element in list1 if element in list2]                                   # List comprehension to find common elements

list1 = list(map(int, input("Enter elements of the first list separated by space: ").split()))  # Taking user input for the first list
list2 = list(map(int, input("Enter elements of the second list separated by space: ").split())) # Taking user input for the second list
print(f"The common elements between the two lists are: {common_elements(list1, list2)}")        # Output the common elements
