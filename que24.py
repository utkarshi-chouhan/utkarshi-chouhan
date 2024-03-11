A = [
    [5,6,7],
    [1,5,9],
    [7,4,5]
]

B= [
    [6,7,9],
    [1,3,4],
    [7,9,1]
]

result =[
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

for i in range (len(A)):
    for j in range (len(A[0])):
        result[i][j]= A[i][j]+B[i][j]
        
for r in result:
    print(r)        