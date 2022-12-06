# 1. Consider there are 2 persons, x and y, We are in problem if x and y are both
#  smiling or if both them are not smiling. Return True if we are in problem.
print("Press y or Y if your ans. is true otherwise n or N")
inp=input("You are smile or not now\n");
inp2=input("You are smile or not now\n")
if(((inp=='y'or inp=='Y') and (inp2=='Y' or inp2=='y')) or ((inp=='n' or inp=='N') and (inp2=='n' or inp2=='N'))):

    print("True")

else:
    print("False")