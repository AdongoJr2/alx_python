def square_matrix_simple(matrix=[]):
    new_matrix = []

    for rowItems in matrix:
        rowSquares = map(lambda n: n ** 2, rowItems)
        new_matrix.append(list(rowSquares))

    return new_matrix
