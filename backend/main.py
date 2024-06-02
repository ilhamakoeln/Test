# Row = int(input("Enter the number of rows:"))
# Column = int(input("Enter the number of columns:"))
 
# # Initialize matrix
# matrix = []
# print("Enter the entries row wise:")
 
# # For user input
# # A for loop for row entries
# for row in range(Row):    
#     a = []
#     # A for loop for column entries
#     for column in range(Column):   
#         a.append(int(input()))
#     matrix.append(a)


# # For printing the matrix
# for row in range(Row):
#     for column in range(Column):
#         print(matrix[row][column], end=" ")
#     print()

n, row, column = map(int, input().split())
matrix = [[0]*n for _ in range(n)]
num = 1
layer = 0


while num <= n*n:
    for i in range(layer, n-layer):
        matrix[layer][i] = num
        num += 1
    for i in range(layer+1, n-layer):
        matrix[i][n-layer-1] = num
        num += 1
    if num <= n*n:
        for i in range(n-layer-2, layer-1, -1):
            matrix[n-layer-1][i] = num
            num += 1
    if num <= n*n:
        for i in range(n-layer-2, layer, -1):
            matrix[i][layer] = num
            num += 1
    layer += 1

