res=input("You are indian if yes press 'y'or 'Y' if not 'n' or 'Y'\n")
age=int(input("Enter your age\n"))
if ((res=='y' or res=='Y') and (age>18)):
    print("Eligible for voting in india")
else:
    print("Not eligible for voting in india")
