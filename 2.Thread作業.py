a = []
b = []

import threading
import time

def sleep5():
    for j in range(int(input("輸入thread次數:"))):
        a.append(j)
        time.sleep(0.5) 
        # print(a)
        
cat = threading.Thread(target=sleep5) 
cat.start() 

for i in range(int(input("輸入main次數:"))):
    b.append(i)
    time.sleep(0.5)
    # print(b)

cat.join()  
print(a ,b)
print("finsh all")
