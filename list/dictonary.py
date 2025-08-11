d1 ={10:20,20:200,30:400,40:500}
d2 ={50:100,40:200,60:700}
for i in d2:
    if i in d1.values():
        d1[i] +=d2[i]
    else:
        d1[i] = d2[i]
print(d1)
print(d2)