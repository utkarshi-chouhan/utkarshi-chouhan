num = int(input("enter the no. of multiples you want for the table of 5:"))
print(f"Table of 5 up to {num} multiples:")
for i in range(1, num+1):
    print(f"5 * {i} = {5 * i}")