#count of vowels in a word

s=input("Enter a Word: ")
s = s.lower()              # converting into lower cased string
vowels_count = 0           # initiating counting variable
for i in s: 
    if i in 'aeiou':       # vowels to count from
        vowels_count += 1        # appending count
print(f"The Number of Vowels in the word {s} is : {vowels_count}") 