l = [39,48,26,98,33,67,87,130,30]

result =list(filter(lambda x : x % 13 ==0,l))

print("the numbers divisible by 13 are",result)