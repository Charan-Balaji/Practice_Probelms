# pyramid pattern with numbers
r=int(input("Enter the number of rows: "))
for i in range(1,r+1):
    print(" " * (r - i) + " ".join(str(j) for j in range(1,i+1)))