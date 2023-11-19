#call_by_value 
def add_1(b):
    b = b + 1
a = 3 
add_1(a) 
print(a) # 應該是4，但沒有return
#因為記憶體大小較小才會被複製另一個地址

#call_by_refernce
def list_adde(b):
    b.append(3)
a=[]
list_adde(a)
print(a)
#因class或list可能檔案很大，所以直接覆蓋在記憶體
#可以用class或list包在內使用