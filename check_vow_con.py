# program that says a character is a vowel or a consonant
def check_vow():
    while(a:='y'):
        c = input("Enter a Character : ")           # reading character from the user 
        c=c.lower()
        if c in 'aeiou':                            # checking condition to be a vowel
            print("It is a Vowel")
        else:
            print("It is a consonant")
        a=input("Do you Want to continue [Y/N] :")
        a=a.lower()

check_vow()                                         # calling our function