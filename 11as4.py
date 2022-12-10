import time
# Write a python program which delays execution of the current thread for 5
#  seconds.
print("1 to 5 numbers")
for s in range(1,6):
    if s==4:
        time.sleep(5)
    print(s)