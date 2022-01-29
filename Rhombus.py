n = int(input("enter number of rows: "))

for i in range(n+1):
 print(" " * ((n+1)-i-1),end="")
 print("*" * (2*i-1),end="")
 print(" " * (n-i-1))

for i in range(n,1,-1):
 print(" " * ((n+1)-(i-1)-1),end="")
 print("*" * (2*(i-1)-1),end="")
 print(" " * ((n-1)-i-1))
