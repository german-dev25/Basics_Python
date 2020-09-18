# 1) Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения
# двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
# строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.


# checking that the matrices are the same
def check_matrix(matrix_1, matrix_2):
    if len(matrix_1) == len(matrix_2):
        for line in range(len(matrix_1)):
            if len(matrix_1[line]) != len(matrix_2[line]):
                return False
    else:
        return False
    return True


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return 'Вывод матрицы\n{}\n'.format('\n'.join(['\t'.join([str(el) for el in row]) for row in self.matrix]))

    def __add__(self, other):
        if check_matrix(self.matrix, other.matrix):
            # create new matrix from the sum of elements of our matrices
            new_matrix = []
            lines = []
            for k in range(len(self.matrix)):
                for i in range(len(self.matrix[k])):
                    lines.append(self.matrix[k][i] + other.matrix[k][i])
                    if len(lines) == len(self.matrix[k]):
                        new_matrix.append(lines)
                        lines = []
            return Matrix(new_matrix)
        else:
            return ('Сложение матриц разных размеров невозможно.\nМогу вывести их в привычном виде\n{}\n\n{}'.
                    format(self, other))


test_print = Matrix([[1, 2, 5], [1, 2, 3], [1, 2, 3, 4]])
print(test_print)

test_m1 = Matrix([[1, 2, 5, 6, 7], [1, 2, 3], [1, 2, 3, 4]])
test_m2 = Matrix([[2, 3, 6, 7, 6], [3, 2, 3], [4, 3, 2, 1]])
test_m3 = Matrix([[3, 4, 5, 6, 5], [2, 1, 1], [3, 4, 3, 2]])
print(test_m1 + test_m2 + test_m3)

test_m4 = Matrix([[2, 3, 6], [3, 2, 3], [4, 3, 2], [5, 5, 5]])
print(test_m3 + test_m4)
