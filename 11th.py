# 11. Consider a tuple t=(3,5,1,9,44,21) , write a Python program which removes
#  number 44 from tuple.
t=(3,5,1,9,44,21)
lt=[]
lt=list(t)
lt.remove(44)
t=tuple(lt)
print(t)