n=int(input ("enter the range of numbers "))
soe=0
soo=0
for i in range(n+1):
    if(i%2==0 and i!=0):
        print(i)
        soe+=i
print(f"the sumof even numbers up to {n} is {soe}")
for i in range(n+1):
    if(i%2!=0 and i!=0):
        print(i)
        soo+=i
print(f"the sum of odd numbers is{soo}")