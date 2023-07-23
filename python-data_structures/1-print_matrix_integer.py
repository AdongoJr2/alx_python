def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        row = matrix[i]
        for j in range(len(row)):
            item = row[j]
            print("{} ".format(item), end="")
        print()
