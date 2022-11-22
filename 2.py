get=int(input("Enter consumed unit of electricity\n"))
if get>=1 and get<=100:
    print("Your electricity bill is :",(get*10))
elif get>=101 and get<=200:
    print("Your electricity bill is :",(get*15))
elif get>=201 and get<=300:
    print("Your electricity bill is :",(get*20))
elif get>300:
    print("Your electricity bill is :",(get*25))
