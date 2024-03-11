x =[
    [1,4,6],
    [5,1,5],
    [3,0,4]
]

result =[
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

for i in range(len(x)):
    for j in range(len(x[0])):
        result[j][i]=x[i][j]
for r in result:
    print(r)