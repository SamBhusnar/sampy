get=int(input("Enter any number\n"))
row=0
colomn=0
while row<get:
    colomn=0
    while colomn<=row:
        print("*",end="")
        colomn=colomn+1
    print()
    row=row+1