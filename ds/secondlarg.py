#
#a_array = [20,30,10,50,35,65,98,44,99]
#a_array.sort()
#print(a_array[-2])
"""def secondlar(a =input(" "),b =" "):
    for i in range(len(a)-1,-1,-1):
        b+=a[i]
    print(b)
    if(b==a):
        print("it is a palndrome")
    else:
        print("not a palndrome")
secondlar()"""
a= input()
rev = a[::-1]
if(rev == a):
    print("true")
else:
    print("false")
print(a[-1::-1])
