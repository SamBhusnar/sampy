# 8. Write a python program which accepts list from user and prints list in
#  descending order.
lt=[]
inp=int(input("How much element you want to insert in list\n"))
for s in range(0,inp):
    get=int(input("Enter any element in list\n"))
    lt.append(get)
lt.sort()
lt.reverse()
print(lt)
