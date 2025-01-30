#number pattern
r=int(input("Enter the number of Rows: "))
for i in range(1,r+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()