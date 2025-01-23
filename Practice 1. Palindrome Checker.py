#verify whether the given word is a palindrome or not.

def is_palindrome(s):                        
    start, end = 0, len(s) - 1               
    while start < end:                       #using while statement to check whether start value is less that end value.
        if s[start] != s[end]:               #using if statement, we check the inequality between start and end of the word.
            return False                     
        start += 1                          
        end -= 1                       
    return True                              

word = input("Enter a word: ")             
if is_palindrome(word):                      #here, we use if statement, that calls the function & verify the condition.
    print("It is a palindrome!")      
else:                                        #if the condition does not satisfies, else part will be executing.
    print("It is not a palindrome.")    
