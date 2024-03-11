num = int(input("enter three digit number :"))
sum=0
temp=num
while(temp>0):
     digit= temp%10
     cube=digit**3
     sum=sum+cube
     temp//=10
if(sum==num):
    print(" it is an armstrong no.")
else:
    print("it is not an armstrong no.")         