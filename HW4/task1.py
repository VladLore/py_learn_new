a = int(input())
matrix = []
for i in range(a):
    b = [int(x) for x in input().split()]
    matrix.append(b)

for j in range(a):
    for k in range(a):
        print(matrix[k][j], end=' ')
    print()