#program to count the number of vowels ina string

def count_vowels(s):                # Function to count vowels in a string
    vowels = 'aeiou'                # Vowel characters
    count = 0                       # Initialize the counter for vowels
    for char in s:                  # Loop through each character in the string
        if char.lower() in vowels:  # If the character is a vowel
            count += 1              # Increment the counter
    return count

string = input("Enter a string: ")  # Taking user input for a string
print(f"The number of vowels in the string is {count_vowels(string)}.")  # Output the count of vowels
