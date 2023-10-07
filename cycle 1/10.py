print("*************************************************")
print("SJC22MCA-2035 : KISHOR VINOD")
print("MCA 2022-24")
print("**************************************************")
def input_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = float(input(f"Enter the element at row {i+1}, column {j+1}: "))
            row.append(element)
        matrix.append(row)
    return matrix

def add_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return None
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            element = matrix1[i][j] + matrix2[i][j]
            row.append(element)
        result.append(row)
    return result

def display_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end="\t")
        print()


rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))


print("Enter elements of the first matrix:")
matrix1 = input_matrix(rows, cols)


print("Enter elements of the second matrix:")
matrix2 = input_matrix(rows, cols)


result_matrix = add_matrices(matrix1, matrix2)

if result_matrix:
    print("\nMatrix 1:")
    display_matrix(matrix1)
    print("\nMatrix 2:")
    display_matrix(matrix2)
    print("\nSum of the matrices:")
    display_matrix(result_matrix)
else:
    print("Matrix addition is not possible. Matrices are of different sizes.")
