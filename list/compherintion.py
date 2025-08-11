"""li = [i for i in range(1,21) if i%2==0]
print(li)
dic ={i: i for i in range(1,11)}
print(dic)

#lamda 
mul = lambda a,b : a*b
print(mul(2,3))
com = lambda a: "even" if a%2 ==0 else "odd"
print(com(20))"""

#map syntax varabel = map(function name,list name as a iterable)
a = [20,34,2,3,45,67,77,33]
result = map(lambda x : x*2, a)
print(list(result))
def type(x):
    if x%2==0:
        return x
ren = map(type,a)
print(list(ren))
#filters syntax result = filter(functionname,iterable like any list name)
def odd(x):
    if x%2 != 0:
        return True
    else:
        return False
num = filter(odd,a)
#with out any function also we can use fliter using lambda
num2 = filter(lambda x: True if x%2!=0 else False,a)
print(list(num))
print(list(num2))
