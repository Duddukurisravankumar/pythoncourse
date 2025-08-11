def information(*args,**kewargs):
    for i in args:
        print(i)
    for i in kewargs:
        print(f"{i} : {kewargs[i]}")
information(123123,213243241123,a=2133,b='jdbcjdbcj',c=739374,)