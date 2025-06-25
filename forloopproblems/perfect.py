# a number whose sum of factors is = to number that is a perfect number
n=int(input("enter thwe number "))
sum=0
for i in range(n):
    if(i!=0 and n%i==0):
        sum+=i
if(sum==n):
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")