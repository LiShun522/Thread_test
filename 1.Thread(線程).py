import threading
import time

def sleep5():
    for j in range(7):
        time.sleep(0.5) # 呼叫sleep設定每次時間，才print
        print("in thread ,  j is "+str(j))
        
cat = threading.Thread(target=sleep5) # 自行取名func
cat.start() # 設定同時執行，sleep5跟接下來的for loop i main迴圈

for i in range(3):
    time.sleep(1)
    print("in main , i is "+str(i))

cat.join()  # 設定main等到cat的therad結束後，才會print end
print("end all")
