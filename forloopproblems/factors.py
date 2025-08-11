n=int(input("enter the number "))
print(f"the factors of {n} are ")
for i in range(n+1):
    if(i!=0 and n%i==0):
        print(i)      