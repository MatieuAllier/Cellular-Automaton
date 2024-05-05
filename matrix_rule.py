import numpy as np

def get_matrix_neighborh(i:int, j:int, matrix:np.matrix):
    """ Get the direct (non diagnal) neighborh of a matrix element

    :param i: the row position of the element
    :param j: the column position of the element
    :param matrix: the matrix
    :returns: the list of all the element neighborh
    :raises keyError: raises an exception
    """
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


def rule_rock_paper_scissor(i:int, j:int, matrix:np.matrix):
    """ Apply rock paper scissor rule to the matrix. With 0 as rock, 1 as paper and 2 a scissor.
    If the element lose against one of its neighborh ti takes it's value.

    :param i: the row position of the element
    :param j: the column position of the element
    :param matrix: the matrix
    :returns: the new value for this position.
    :raises keyError: raises an exception
    """
    list_neighboor = get_matrix_neighborh(i, j, matrix)
    element = matrix[i, j]
    # Case rock vs paper
    if element == 0 and 1 in list_neighboor:
        return 1
    # Case paper vs scissor
    elif element == 1 and 2 in list_neighboor:
        return 2
    # Case scissor vs rock
    elif element == 2 and 0 in list_neighboor:
        return 0
    return element


def apply_rule_to_matrix(matrix:np.matrix, rule_function: callable):
    """ Apply a rule function to an entire matrix

    :param matrix: the matrix
    :param rule_function : the function to apply at the entire matrix
    :returns: the new value for this position.
    :raises keyError: raises an exception
    """
    n = len(matrix)
    new_matrix = matrix.copy()
    for i in range(0, n):
        for j in range(0, n):
            new_matrix[i, j] = rule_function(i, j, matrix)
    return new_matrix

if __name__ == "__main__":
    random_matrix = np.asmatrix(np.random.randint(3, size=(100,100)))
    print(random_matrix)
    print(apply_rule_to_matrix(random_matrix, rule_rock_paper_scissor))