
n = int(input("enter number of rows: "))  
j=n
for i in range(1,n+1):
 print(" " * i,end="")
 print("*" * j,end="")
 print("")
 j-=1
    
