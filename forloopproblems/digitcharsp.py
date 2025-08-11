a ="ajfkdio129838@#*$&$^%!@jhdihdikjdea123449753"
digit =0
char =0
spch =0
for i in a:
    if i.isdigit():
        digit+=1
    elif i.isalpha():
        char+=1
    else:
        spch+=1
print(digit,char,spch)
        