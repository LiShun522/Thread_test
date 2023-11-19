from threading import Thread
import time

def th1_run(total):
    a = []
    for i in range(total):
        a.append(i)
        time.sleep(0.5)
    print(a)

th1 = Thread(target=th1_run,args = (int(input("輸入")),))
th1.start()

b = []
for j in range(3):
    b.append(j+1)
    time.sleep(0.5)
print(b)
th1.join()
print("finsh all")