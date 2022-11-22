get=int(input("Enter any number\n"))
save=0
for s in range(1,get+4):
    if get%s==0:
        save=save+1
    if s==get+1:
        break
else:
    print("Workd is done")
print("Factor of this number is :",save)