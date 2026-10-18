a=4
b=5
c=7
def greatest (a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c

print(greatest(a,b,c))