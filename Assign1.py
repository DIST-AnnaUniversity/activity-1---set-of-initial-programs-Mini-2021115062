#1
def num(a,b):
    if a==b:
        print(a)
        return a
    else:
        print(a,end=" ")
        return(num(a+2,b))
num(1,9)
#2
def num(a,b):
    if a==b:
        print(a)
        return a
    else:
        print(a,end=" ")
        return(num(a+3,b))
num(3,12)
#3
def num(a,b):
    if a==b:
        print(a)
        return a
    else:
        print(a,end=" ")
        return(num(a*3,b))
num(3,81)
#4
def num(a,b):
    if a==b:
        print(a)
        return a
    else:
        print(a,end=" ")
        return(num(a+6,b))
num(1,25)
#5
def num(a,b):
    if a==b:
        print(a)
        return a
    else:
        print(a,end=" ")
        return(num(a*2,b))
num(1000,8000)
#6
def num(a,b):
    if a==b:
        print(a)
        return a
    else:
        print(a,end=" ")
        return(num(a*(3/4),b))
num(7,189/64)
#7
def num(a,b):
    if a==b:
        print(a)
        return a
    else:
        print(a,end=" ")
        return(num(a+2),b)
num(0,10)

