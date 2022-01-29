n = int(input("enter number of rows: "))

# for i in range(1,n+1): 
#      x=2*i-1   
#      for j in range(i,2*n):
#         print(end=" ")

#      for k in range(1,x+1):
#         print("*",end=" ")    

#      print(" ")      
for i in range(n+1):
 print(" " * ((n+1)-i-1),end="")
 print("*" * (2*i-1),end="")
 print(" " * (n-i-1))

