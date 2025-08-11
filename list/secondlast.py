li = [12,15,34,45,33,1,2,3]
largest  =li[0]
secondlarge =li[0]
for i in li:
    if i> largest:
        secondlarge =largest
        largest =i
    elif i > secondlarge:
        secondlarge = i
print(largest,secondlarge)
'''li= [12,34,25,46,57,89,100,23,45,26,66,78,90,45]
li.sort()
print(li[-2])'''