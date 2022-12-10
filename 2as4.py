# 2. Write a python function which accepts three values, return their sum
# #  if and only if three values are not similar. 
def myfucn(a,b,c):
    if( a is  b is c):
        print("All value are similar!")
    else:
        print("Sum is :",(a+b+c))
inp=int(input("Enter any number"))
inp2=int(input("Enter any number"))
inp3=int(input("Enter any number"))
myfucn(inp,inp2,inp3)