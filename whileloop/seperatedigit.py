a=int(input("enter the number "))
rev=0
while a> 0:
    b=a%10
    a=a//10
    rev=rev*10 + b
    print(b)
print(rev)
    
    