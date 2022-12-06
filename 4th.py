# Write a program to get a string from user and swap the first and last
#  character of string.

get=input("Enter any string\n")
save=get[:1:1]
save2=get[-1:-2:-1]
newget=get
print(len(get))
save3=newget[1:len(get)-1:1]
newget2=save2+save3+save
print(save,save2)
print(newget2)
