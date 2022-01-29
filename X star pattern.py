n = int(input("enter number of rows: "))
m=2*n-1
for i in range(1,m+1):
    for j in range(1,m+1):
        if i==j or j==m-i+1 :
            print("*",end="")
        else:
            print(" ",end="")

    print()
 