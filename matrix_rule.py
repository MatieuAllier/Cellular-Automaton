import numpy as np

def get_matrix_neighborh(i:int, j:int, matrix):
    n = len(matrix)-1
    list_neighborh = []
    if i != 0:
        list_neighborh.append(matrix[i-1,j])
    if i != n:
        list_neighborh.append(matrix[i+1,j])
    if j != 0:
        list_neighborh.append(matrix[i,j-1])
    if j != n:
        list_neighborh.append(matrix[i,j+1])
    return list_neighborh

if __name__ == "__main__":
    matrix = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(matrix)
    print(get_matrix_neighborh(0,1,matrix))