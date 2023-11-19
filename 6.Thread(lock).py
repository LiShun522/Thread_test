import threading
import time
accountMoney = 1000
def atm_action(atmLock):  #
    global accountMoney
    atmLock.acquire(timeout = 1)  # 怕有deadlock所以要設定時間
    print("ready get money")
    moneyFromServer = accountMoney # 領前下載資料
    time.sleep(1)
    moneyFromServer -= 100
    print("final account money is " + str(moneyFromServer))
    time.sleep(1)
    accountMoney = moneyFromServer # 領完上傳回去
    atmLock.release()

atmLock = threading.Lock() #
atm1 = threading.Thread(target=atm_action,args=(atmLock,))
atm2 = threading.Thread(target=atm_action,args=(atmLock,))
atm1.start()
atm2.start()
atm1.join()
atm2.join()
print(accountMoney)

# 思考兩個程式怎麼執行