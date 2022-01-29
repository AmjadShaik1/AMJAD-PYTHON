n = int(input("Enter any number: "))
temp = n
sum = 0
while(temp!=0):
 
    rem = temp%10
    sum = sum+(rem*rem*rem) 
    temp=temp//10

if (sum==n):
    print("%d is an Armstrong number "  %n)

else:
    print("%d is not  an Armstrong number "  %n)
  


