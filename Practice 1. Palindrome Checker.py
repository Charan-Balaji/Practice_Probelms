#verify whether the given word is a palindrome or not.

def is_palindrome(s):                        #here i'm defining a function to check whether word is palindrome.
    start, end = 0, len(s) - 1               #defining the necessary variables.
    while start < end:                       #using while statement to check whether start value is less that end value.
        if s[start] != s[end]:               #using if statement, we check the inequality between start and end of the word.
            return False                     #returning false id the don't match.
        start += 1                           #Moving the start pointer towards the right .
        end -= 1                             #moving the end pointer towards the left.
    return True                              #If the loop completes without returning False, the string is a palindrome.

word = input("Enter a word: ")               #in this line, we are getting input form the user.
if is_palindrome(word):                      #here, we use if statement, that calls the function & verify the condition.
    print(f"{word} is a palindrome!")        #this print statement will executes when the word is actually palindrome.
else:                                        #if the condition does not satisfies, else part will be executing.
    print(f"{word} is not a palindrome.")    #this print statement will executes when the word is not a palindrome.
