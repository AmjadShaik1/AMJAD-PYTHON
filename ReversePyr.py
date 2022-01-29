# from tkinter import Y


# n = int(input("enter number of rows: "))
# y=n+1
# x=y*2-1
# for i in range(1,y): 
   
#     for j in range(1,i):
#         print(" ",end="")

#     for k in range(i,x+1):
#         print("* ",end="")    

#     print(" ")  

n = int(input("enter number of rows: "))  
for i in range(n+1,1,-1):
 print(" " * ((n+1)-(i-1)-1),end="")
 print("*" * (2*(i-1)-1),end="")
 print(" " * (n-i-1))

    
