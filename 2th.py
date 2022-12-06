#  Input a string, return a new string where "not " has been added to the front.
#  but, if the string already begins with "not", return the string unchanged.

get=input("Enter any string\n")
save=get.startswith("not")
if(save==True):
    print(get)
else:
    newGet="not"+get
    print(newGet)
