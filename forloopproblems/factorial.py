n =int(input())
fact=1
for i in range(n+1):
    if(i>0):
        fact=fact*i
print(f"THe factorial of the {n} is {fact}")