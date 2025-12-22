import numpy as np
from hw3.matrix import Matrix


def main():
    hashes = {}
    np.random.seed(0)

    while True:
        np_matrix = np.random.randint(0, 10, (10, 10))
        matrix = Matrix(np_matrix)
        h = hash(matrix)
        if h in hashes:
            a = matrix
            c = hashes[h]
            break
        hashes[h] = matrix


    b = d = Matrix(np.random.randint(0, 10, (10, 10)))

    ab = a @ b
    cd = c @ d

    a.to_file('artifacts/A.txt')
    b.to_file('artifacts/B.txt')
    c.to_file('artifacts/C.txt')
    d.to_file('artifacts/D.txt')
    ab.to_file('artifacts/AB.txt')
    cd.to_file('artifacts/CD.txt')


if __name__ == "__main__":
    main()