#program to count the number of vowels ina string

def count_vowels(s):                
    vowels = 'aeiou'                
    count = 0                     
    for char in s:                  # Loop through each character in the string
        if char.lower() in vowels:  # If the character is a vowel
            count += 1              # Increment the counter
    return count

word = input("Enter a string: ") 
print("The number of vowels in the string is", count_vowels(word))  # Output the count of vowels
