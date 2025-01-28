# reversing a string without using slicing
def rev_str(s):
    r = ""
    for i in range (len(s)-1,-1,-1): # looping from the reverse direction
        r += s[i]                    # appending the reversed char
    return r

s = input("Enter a String : ")       # getting input from the user
reversed_str = rev_str(s)
print("The reversed string is : ", reversed_str)



