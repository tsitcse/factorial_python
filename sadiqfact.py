def rec_fact(n):
    if n<=1:
        return n
    else:
        return n* rec_fact(n-1)


num=7
if n<=0:
    print("cant perform value is nagitive")
else:
    print("the factorial is" n,"is"rec_fact(n))
