class Processor:

    def __init__(self, dimension):
        self.dimensions = [int(i) for i in dimension]
        self.rows = self.dimensions[0]
        self.columns = self.dimensions[1]
        self.matrix1 = []
        self.matrix2 = []
        self.identity = []
        self.product_matrix = []

    def create_matrix_1(self):
        print('Enter first matrix:')
        for r in range(self.rows):
            self.matrix1.append([])
            entry = input().split()
            for c in range(0, self.columns):
                self.matrix1[r].append(float(entry[c]))
        return self.matrix1

    def create_matrix_2(self, dimension):
        dimensions = [int(i) for i in dimension]
        rows = dimensions[0]
        columns = dimensions[1]
        print('Enter second matrix:')
        for r in range(rows):
            self.matrix2.append([])
            entry = input().split()
            for c in range(0, columns):
                self.matrix2[r].append(float(entry[c]))
        return self.matrix2

    def create_identity(self):
        for i in range(0, self.rows):
            self.identity.append([])
            for j in range(0, self.columns):
                if j == i:
                    self.identity[i].append(1)
                else:
                    self.identity[i].append(0)
        self.matrix2 = self.identity

    def add_matrices(self):
        if len(self.matrix2) != self.rows or len(self.matrix2[0]) != self.columns:
            print('The operation cannot be performed.', '\n')
        else:
            for r in range(self.rows):
                self.product_matrix.append([])
                for c in range(0, self.columns):
                    self.product_matrix[r].append(self.matrix1[r][c] + self.matrix2[r][c])
            processor.print_matrix()

    def multiply_matrix(self, multiple):
        for r in range(self.rows):
            self.product_matrix.append([])
            for c in range(0, self.columns):
                self.product_matrix[r].append(self.matrix1[r][c] * multiple)
        processor.print_matrix()

    def multiply_matrices(self):
        if len(self.matrix1[0]) != len(self.matrix2):
            print('The operation cannot be performed.', '\n')
        else:
            for r in range(self.rows):
                self.product_matrix.append([])
                for column in range(len(self.matrix2[0])):
                    total = 0
                    for num in range(self.columns):
                        total += self.matrix1[r][num] * self.matrix2[num][column]
                    self.product_matrix[r].append(total)
            processor.print_matrix()

    def transpose_matrix(self, trans_choice):
        transform_choice = trans_choice
        if transform_choice == 1:
            for r in range(self.columns):
                self.product_matrix.append([])
                for c in range(self.rows):
                    self.product_matrix[r].append(self.matrix1[c][r])
            return self.product_matrix
        elif transform_choice == 2:
            for r in range(self.rows):
                self.product_matrix.append([])
            for r in range(self.rows):
                i = self.rows - 1 - r
                new_row = []
                for column in range(self.columns):
                    j = self.columns - 1 - column
                    new_row.append(self.matrix1[j][i])
                self.product_matrix[r] = new_row
        elif transform_choice == 3:
            for r in range(self.rows):
                self.product_matrix.append([])
                self.product_matrix[r] = self.matrix1[r][::-1]
        elif transform_choice == 4:
            for r in range(self.rows):
                self.product_matrix.append([])
            i = 0
            for r in reversed(range(self.rows)):
                self.product_matrix[r] = (self.matrix1[i][::1])
                i += 1

    def find_det(self, matrix_a):
        if self.columns != self.rows:
            print('Cannot perform operation.')
            pass
        elif self.columns == 1 and self.rows == 1:
            return self.matrix1[0][0]
        else:
            total = 0
            indices = list(range(len(matrix_a)))
            if len(matrix_a) == 2 and len(matrix_a[0]) == 2:
                val = matrix_a[0][0] * matrix_a[1][1] - matrix_a[1][0] * matrix_a[0][1]
                return val
            for focus in indices:
                sub_mat = matrix_a[:]
                sub_mat = sub_mat[1:]
                height = len(sub_mat)
                for i in range(height):
                    sub_mat[i] = sub_mat[i][0:focus] + sub_mat[i][focus + 1:]
                sign = (-1) ** (focus % 2)
                sub_det = processor.find_det(sub_mat)
                total += sign * matrix_a[0][focus] * sub_det
            return total

    def get_minor(self, m, i, j):
        return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]

    def inverse(self, d, a_matrix):
        if len(a_matrix) == 2:
            return [[a_matrix[1][1] / d, -1 * a_matrix[0][1] / d],
                    [-1 * a_matrix[1][0] / d, a_matrix[0][0] / d]]
        cofactors = []
        for r in range(len(a_matrix)):
            cofactor_row = []
            for c in range(len(a_matrix)):
                minor = processor.get_minor(a_matrix, r, c)
                cofactor_row.append(((-1) ** (r + c)) * processor.find_det(minor))
            cofactors.append(cofactor_row)
        self.matrix1 = cofactors
        processor.transpose_matrix(1)
        for r in range(len(self.product_matrix)):
            for c in range(len(self.product_matrix)):
                self.product_matrix[r][c] = self.product_matrix[r][c] / d

    def print_matrix(self):
        print('The result is: ')
        for r in range(0, len(self.product_matrix)):
            print(*self.product_matrix[r])
        print()


user_input = None
while user_input != 0:
    print('1. Add matrices\n'
          '2. Multiply matrix by a constant\n'
          '3. Multiply matrices\n'
          '4. Transpose matrix\n'
          '5. Calculate a determinant\n'
          '6. Inverse matrix\n'
          '0. Exit')
    user_input = int(input('Your choice: '))
    if user_input == 1:
        processor = Processor(input('Enter size of first matrix: ').split())
        processor.create_matrix_1()
        processor.create_matrix_2(input('Enter size of second matrix: ').split())
        processor.add_matrices()
    elif user_input == 2:
        processor = Processor(input('Enter matrix size: ').split())
        processor.create_matrix_1()
        print('Multiply by: ')
        processor.multiply_matrix(int(input()))
    elif user_input == 3:
        processor = Processor(input('Enter size of first matrix: ').split())
        processor.create_matrix_1()
        processor.create_matrix_2(input('Enter size of second matrix: ').split())
        processor.multiply_matrices()
    elif user_input == 4:
        print('1. Main diagonal\n'
              '2. Side diagonal\n'
              '3. Vertical line\n'
              '4. Horizontal line')
        choice = int(input('Your choice: '))
        processor = Processor(input('Enter matrix size: ').split())
        processor.create_matrix_1()
        processor.transpose_matrix(choice)
        processor.print_matrix()
    elif user_input == 5:
        processor = Processor(input('Enter matrix size: ').split())
        A = processor.create_matrix_1()
        print('Your result is:\n', str(processor.find_det(A)))
    elif user_input == 6:
        processor = Processor(input('Enter matrix size: ').split())
        matrix = processor.create_matrix_1()
        processor.create_identity()
        det = processor.find_det(matrix)
        if det == 0:
            print("This matrix doesn't have an inverse.\n")
        else:
            processor.inverse(det, matrix)
            processor.print_matrix()
    elif user_input == 0:
        print('Bye!')
        quit()
    else:
        continue
