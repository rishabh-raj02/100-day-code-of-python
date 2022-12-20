import time
print(time.gmtime(0))
curr=time.time()
print("current time in seconds= ",curr)
for i in range (4):
    time.sleep(1)
    print(i)