import random 
import time 


time_to_sleep = random.randint(1,60)
print(time_to_sleep)
for i in range(time_to_sleep):
    print(i)
    time.sleep(1)
    
time.sleep(time_to_sleep)    