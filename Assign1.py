#1
m=int(input("ENTER NUMBER 1:"))
n=int(input("ENTER NUMBER 2:"))
print("The sum is:",m+n)

#2
n=int(input("ENTER NUMBER:"))
fac=1
for i in range(1,n+1,1):
    fac*=i
print("The factorial of ",n,"is ",fac)

#3
n=int(input("ENTER NUMBER:"))
sum=n*(n+1)/2
print("The sum of ",n,"numbers is ",sum)

#4
s=input("ENTER STRING:")
vowel=0
for i in s:
    if i.upper() in ["A","E","I","O","U"]:
        vowel+=1
print("Number of vowels are ",vowel)

#5
n=int(input("Enter number:"))
if n%2==0:
    print("EVEN")
else:
    print("ODD")

#6
n=int(input("ENTER NUMBER:"))
d=0
while(n!=0):
    d+=1
    n=n//10
print("No. of digits:",d)

#7
n=int(input("ENTER NUMBER:"))
print("square:",n*n ,"\ncube: ",n*n*n,"\ncuberoot:",n**(1/3))

#8
n=int(input("ENTER NUMBER:"))
sum=0
while(n!=0):
    x=n%10
    sum+=x
    n=n//10
print("Sum of digits:",sum)

#9
n=int(input("ENTER NUMBER:"))
print("reverse:")
while(n!=0):
    x=n%10
    print(x,end = "")
    n=n//10
   
#10
n=int(input("ENTER NUMBER:"))
p=int(input("ENTER POWER:"))
val=(1-n**(n+1))/(1-n)
print(val)
