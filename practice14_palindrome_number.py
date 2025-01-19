#check whether the given number is a palindrome or not
def is_palindrome(n):                        # Function to check if the number is a palindrome
    original = n                             # Store the original number
    reversed_n = 0                           # Initialize variable to store the reversed number
    while n > 0:                             # Loop until the number becomes 0
        digit = n % 10                       # Get the last digit
        reversed_n = reversed_n * 10 + digit # Build the reversed number
        n //= 10                             # Remove the last digit
    return original == reversed_n            # Check if the reversed number matches the original number

number = int(input("Enter a number: "))      # Taking user input for the number
if is_palindrome(number):                    # Check if the number is a palindrome
    print(f"{number} is a palindrome.")      # Output if the number is palindrome
else:                                        # If the number is not a palindrome
    print(f"{number} is not a palindrome.")  # Output if the number is not palindrome
