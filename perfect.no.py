n = int (input("enter any number: "))
sum = 0
for j in range(1,n):
 if n%j==0:
    sum+=j
if sum == n :
    print("Perfect number")
else:
    print("Not a Perfect number")

