'''
Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.


'''

def transposeMatrix(matrix):
    # Write your code here.
    newMatrix=[]
    row=len(matrix)
    col=len(matrix[0])
    for i in range(col):
        temp=[]
        for j in range(row):
            temp.append(matrix[j][i])
        newMatrix.append(temp)
    return newMatrix
  