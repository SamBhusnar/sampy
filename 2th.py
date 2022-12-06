get=input("Enter any string\n")
save=get.startswith("not")
if(save==True):
    print(get)
else:
    newGet="not"+get
    print(newGet)
