s = "1.23,3.45,5.67,90.3,7.1"
a = ""
c = 0

for i in s:
    #print(i)
    if i != ",":
        a = a + i
    else:
    #elif i == ",":
        #b = b + float(a)
        c = c + float(a)
        a = ""
        
c = c + float(a)    
print(c)
    
