
def call_test(a,b):
    for i in range(a):
        i = i *2 + 2
        b.append(i)
    
a = 10
b = []    
call_test(a,b)
print(b)
