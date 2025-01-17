#program to reverse a string
def reverse_string(s):                     # Function to reverse the string
    reversed_str = ""                      # Initialize an empty string to store the reversed string
    for char in s:                         # Loop through each character in the input string
        reversed_str = char + reversed_str # Add each character at the beginning of reversed_str
    return reversed_str                    # Return the reversed string

string = input("Enter a string: ")         # Taking user input for string
print(f"The reversed string is: {reverse_string(string)}.")  # Output the reversed string
