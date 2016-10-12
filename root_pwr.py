x = int(input("Enter a number: "))
r, p = 0, 2
bool = True

while bool:
    r = r + 1
    if r**p > abs(x) and p < 6:
        r, p = 0, p + 1
    elif r**p >= abs(x):
        bool = False
        
if r**p == abs(x):
    print("The root and power of",x,"is",r,"and",p)
else:
    print("No root for",x)