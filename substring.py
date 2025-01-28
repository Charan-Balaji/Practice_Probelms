# Substring program 

s1='har'                               # input string (or) original string
for i in range(len(s1)):               # iteration with length as range
    for j in range(i+1, len(s1)+1):    # iteration with other variable using length + 1
        print(s1[i:j])                 # printing the substrings --> output