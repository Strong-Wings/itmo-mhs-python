import operator
import numpy as np
from hw3.matrix import Matrix


def execute(np_matrix1, np_matrix2, op):
    ops = {
        '+': operator.add,
        '*': operator.mul,
        '@': operator.matmul,
    }

    matrix1 = Matrix(np_matrix1)
    matrix2 = Matrix(np_matrix2)

    with open(f'artifacts/matrix{op}_np.txt', 'w') as f:
        print(ops[op](np_matrix1, np_matrix2), file=f)

    ops[op](matrix1, matrix2).to_file(f'artifacts/matrix{op}.txt')


def main():
    np.random.seed(0)

    np_matrix1 = np.random.randint(0, 10, (10, 10))
    np_matrix2 = np.random.randint(0, 10, (10, 10))

    execute(np_matrix1, np_matrix2, '+')
    execute(np_matrix1, np_matrix2, '*')
    execute(np_matrix1, np_matrix2, '@')
    execute(np_matrix1, np_matrix2, '@')

if __name__ == "__main__":
    main()