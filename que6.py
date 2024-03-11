num = int(input("enter any number:"))
isprime = True

if num > 1:
    for i in range(2,int(num**0.5)+1):
        if (num%i)==0:
            print(num, "is composite number")
            isprime = False
            break
elif num==0 or 1:
    print(num,"is a neither prime NOR  composite number")
else:
    print(num,"it is a composite number")
    
if(isprime):
    print(num,"is prime")