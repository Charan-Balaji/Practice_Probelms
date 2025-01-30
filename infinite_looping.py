# Imagine you‟re on a quest to discover never-ending loops. Create a program that demonstrates two types of endless journeys: 
# one using a for loop and another using a  while loop. How will you set up these loops to keep running forever, showcasing their infinite nature?


import itertools

def infinite_for_loop():            # Infinite for loop using itertools.cycle()
    for _ in itertools.cycle([1]):  # this will loop infinitely 
        print("For Loop: Running forever...")

def infinite_while_loop():          # # Infinite while loop when true
    while True:
        print("While Loop: Running forever...")

infinite_for_loop()   # we can call any one function, as this program will run loop infinitely 
# infinite_while_loop()
