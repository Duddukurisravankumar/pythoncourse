"""def sum():
    a =int(input())
    b=int(input())
    print(a+b)
sum()"""
#parameters
"""def sum(a,b):
    print(a+b)
sum(1,2)"""
#default arguments
def sum(a=10,b=30):
    print(f"your sum is {a+b}")
sum(0,30)