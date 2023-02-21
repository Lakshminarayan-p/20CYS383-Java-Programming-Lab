n=int(input("enter the number:"))
f=0
while n>0:
    a=n%10
    if a%2==0:
        f=f+1
    n=n//10
print(f)
        
