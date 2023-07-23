def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        row = matrix[i]
        for j in range(len(row)):
            item = row[j]
            if j == (len(row) - 1):
                print("{:d}".format(item), end="")
            else:
                print("{:d} ".format(item), end="")
        print()
