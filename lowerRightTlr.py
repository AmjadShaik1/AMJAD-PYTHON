
n = int(input("enter number of rows: "))  
j=1
for i in range(n+1,1,-1):
 print(" " * i,end="")
 print("*" * j,end="")
 print("")
 j+=1
    
