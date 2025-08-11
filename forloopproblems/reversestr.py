n =input ("enter the string")
b =""
for i in range(len(n)-1,-1,-1):
    b +=n[i]
print(b)
if(b==n):
    print(f"{n} is palndrome")
    