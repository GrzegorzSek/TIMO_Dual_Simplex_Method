# Dual Simplex Method

# Imports
import numpy as np


def main():
    a = np.array([[0., 1., 1.], [-8., -1., -2.], [-6., -2., -1.], [-5., -1., -1.]])
    rows: int = a.shape[0]
    cols: int = a.shape[1]

    is_a = is_acceptable(cols, a)

    if is_a:
        print('Rozwiązanie jest dualnie dopuszcalne')
        is_b = is_optimal(rows, a)

        while not is_b:
            print('Rozwiązanie jest nieoptymalne')
            row_of_variable_removed_from_base = variable_to_remove(rows, a)  # wiersz zmiennej do usunięcia
            print('wiersz:' + str(row_of_variable_removed_from_base))
            col_of_variable_added_to_base = variable_to_add(cols, a, row_of_variable_removed_from_base)
            print('kolumna:' + str(col_of_variable_added_to_base))
            a = gaussian_elimination(a, row_of_variable_removed_from_base, col_of_variable_added_to_base, rows, cols)

            # is_b = is_optimal(rows, a)
            is_b = True  # na czas testów jest True, żeby była tylko jedna iteracja
            print(a)
    else:
        print('Rozwiązanie nie jest dualnie dopuszczalne')


def is_acceptable(cols, a):  # test dualnej dopuszczalności zaczyna się od wiersza zerowego
    for i in range(cols):
        if a[0, i] < 0:
            return False
    return True


def is_optimal(rows, a):  # test optymalności zaczyna się od wiersza 1 nie od zerowego
    for i in range(rows):
        if a[i, 0] < 0:
            return False
    return True


def variable_to_remove(rows, a):
    x = a[1, 0]
    row = 1
    for i in range(1, rows - 1):
        if x > a[i+1, 0]:
            x = a[i+1, 0]
            row += 1
    # print(x)
    return row


def variable_to_add(cols, a, row):
    new_starting_point = 0
    x = 0
    col = 1

    for i in range(1, cols):
        if a[row, i] < 0:
            x = a[0, 1] / a[row, i]
            # print(x)
            new_starting_point += 1
            # print(new_starting_point)
            break

    for i in range(new_starting_point, cols - 1):
        if a[row, i + 1] < 0 and a[0, i] / a[row, i+1] > x:
            x = a[0, i] / a[row, i+1]
            col += 1
    # print(col)
    return col


def gaussian_elimination(a, row, col, rows, cols):
    b = a
    for i in range(0, rows):  # wiersze
        for j in range(0, cols):  # kolumny
            if i == row and j == col:
                a[i, j] = 1 / b[i, j]
            elif i == row and j < col:
                a[i, j] = b[row, j] / b[row, col]
            elif i < row and j == col:
                a[i, j] = -b[i, col] / b[row, col]
            else:
                print(b)
                # print(b[i, j], '-', b[i, col], '*', b[row, j], '/', b[row, col])
                a[i, j] = b[i, j] - b[i, col] * b[row, j] / b[row, col]
    return a


if __name__ == '__main__':
    main()
