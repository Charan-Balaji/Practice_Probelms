#check whether the given number is a palindrome or not
def is_palindrome(n):                       
    original = n                           
    reversed_n = 0                          
    while n > 0:                            
        digit = n % 10                      
        reversed_n = reversed_n * 10 + digit 
    return original == reversed_n           

number = int(input("Enter a number: "))      
if is_palindrome(number):                   
    print(f"{number} is a palindrome.")      
else:                                        
    print(f"{number} is not a palindrome.")  
