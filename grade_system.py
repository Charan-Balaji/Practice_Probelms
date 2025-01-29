#write a python program that takes score as input and prints out the corresponding grade according to the following scheme
#90 and above: A
#80-89 : B
#70-79: C
#60-69: D
#below 60: F

def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Taking user input

score = float(input("Enter the score: "))
if 0 <= score <= 100:
    print(f"Grade: {get_grade(score)}")
else:
    print("Please enter a valid score between 0 and 100.")

