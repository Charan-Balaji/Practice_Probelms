#pattern program diamond
def print_pattern(size):
    # Upper triangle
    for i in range(1, size + 1):
        print(" " * (size - i) + "* " * i)

    # Lower triangle
    for i in range(size, 0, -1):
        print(" " * (size - i) + "* " * i)

size = 7
print_pattern(size)
