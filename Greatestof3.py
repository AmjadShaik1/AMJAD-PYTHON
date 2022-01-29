a = int (input("enter first number: "))
b = int (input("enter second number: "))
c = int (input("enter third number: "))

if a>b:
    if a>c:
        print( a, "is greater than" ,b,",",c)
    else:
        print( c, "is greater than" ,a,",",b)

elif b>c:
    print( b, "is greater than" ,a,",",c)
else:
        print( c, "is greater than" ,a,",",b)

