
def call_test(a,b):
    for i in range(a):
        i = i *2 + 2
        b.append(i)
    
a = 5
b = []    
call_test(a,b)
print(a)
print(b)

#老師解說
def func(var,lis,c):
    for i in range(var):
        lis.append((i+1)*2)
    
    c.append(lis[var-1])

a = 5 
b = []
c = []
func(a,b,c)
print(c[0])
print(a)
print(b) 
