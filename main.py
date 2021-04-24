# Dual Simplex Method

# Imports
import numpy as np


def main():
    a = np.array([[0., 1., 1.], [-8., -1., -2.], [-6., -2., -1.], [-5., -1., -1.]])

    a_dict = {}
    a_dict2 = {}
    a_goal = [0, 1, 2]
    a_support = [0, 3, 4, 5]
    rows: int = a.shape[0]
    cols: int = a.shape[1]
    print(rows, cols)

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
            swap_x(a_goal, a_support, row_of_variable_removed_from_base, col_of_variable_added_to_base)

            is_b = is_optimal(rows, a)
            # is_b = True  # na czas testów jest True, żeby była tylko jedna iteracja
            # print(a)

        print("macierz wyników")
        print(a)
        print()

        print("tabele pomocnicze")
        print("f celu: ")
        print(a_goal)
        print("zm pomocnicze: ")
        print(a_support)
        print()

        print("wynik jako dictionary")
        answer_dict(a, a_goal, a_support, a_dict)
        print(a_dict)

        print("wynik jako wektor")
        ans1 = []
        answer_array(a_dict, ans1)
        print(ans1)
        print()

        # po rozwiązaniu sprawdzamy czy ma zero w funckji celu i wykonujemy odpowiednie akcje
        has_inf_solutions = is_multiple_solutions(a, cols)
        if has_inf_solutions:
            col_no = col_to_opt(a, cols)
            row_no = row_to_simplex(a, rows, col_no)
            a = gaussian_elimination(a, row_no, col_no, rows, cols)
            swap_x(a_goal, a_support, row_no, col_no)

            print("macierz wyników")
            print(a)
            print()

            print("tabele pomocnicze")
            print("f celu: ")
            print(a_goal)
            print("zm pomocnicze: ")
            print(a_support)
            print()

            print("wynik jako dictionary")
            answer_dict(a, a_goal, a_support, a_dict2)
            print(a_dict2)

            print("wynik jako wektor")
            ans2 = []
            answer_array(a_dict2, ans2)
            print(ans2)
            print()

    else:
        print('Rozwiązanie nie jest dualnie dopuszczalne')


def answer_dict(a, a_goal, a_support, a_dict):
    for i in range(1, len(a_goal)):
        a_dict[a_goal[i]] = a[0, i]

    for j in range(1, len(a_support)):
        a_dict[a_support[j]] = a[j, 0]


def answer_array(a_dict, ans):
    for i in range(1, len(a_dict)+1):
        ans.append(a_dict.get(i))


def swap_x(goal, support, row, col):
    temp = goal[col]
    goal[col] = support[row]
    support[row] = temp


def is_acceptable(cols, a):  # test dualnej dopuszczalności zaczyna się od wiersza zerowego
    for i in range(cols):
        if a[0, i] < 0:
            return False
    return True


def is_optimal(rows, a):  # test optymalności zaczyna się od wiersza 1 nie od zerowego
    for i in range(1, rows):
        if a[i, 0] < 0:
            return False
    return True


def is_multiple_solutions(a, cols):  # sprawdzamy czy f. celu ma zero
    for i in range(1, cols):
        if a[0, i] == 0:
            return True


def col_to_opt(a, cols):  # bierzemy kolumnę dla której jest zero
    for i in range(1, cols):
        if a[0, i] == 0:
            return i


def row_to_simplex(a, rows, col):  # szukamy dla jakie zmienne musimy ze sobą zamienić dla wielu rozw.
    x = 0
    x_i = 0
    row_output = 0

    for i in range(1, rows):
        if a[i, 0] / a[i, col] >= 0:
            x = a[i, 0] / a[i, col]
            row_output = i
            x_i = i + 1

    if x_i <= rows:
        for j in range(x_i, rows):
            if a[j, 0] / a[j, col] >= 0:
                y = a[j, 0] / a[j, col]
                if y < x:
                    x = a[j, 0] / a[j, col]
                    row_output = j

    return row_output


def variable_to_remove(rows, a):
    x = a[1, 0]
    row = 1
    for i in range(1, rows - 1):
        if x > a[i + 1, 0]:
            x = a[i + 1, 0]
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
        if a[row, i + 1] < 0 and a[0, i] / a[row, i + 1] > x:
            x = a[0, i] / a[row, i + 1]
            col += 1
    # print(col)
    return col


def gaussian_elimination(a, row, col, rows, cols):
    b = a.copy()
    for i in range(0, rows):  # wiersze
        for j in range(0, cols):  # kolumny
            if i == row and j == col:
                a[i, j] = 1 / b[i, j]
            elif i == row and j != col:
                a[i, j] = b[row, j] / b[row, col]
            elif i != row and j == col:
                a[i, j] = -b[i, col] / b[row, col]
            else:
                # print(b)
                # print(b[i, j], '- (', b[i, col], '*', b[row, j], '/', b[row, col], ')')
                a[i, j] = b[i, j] - b[i, col] * b[row, j] / b[row, col]
                # print(a[i, j])
    return a


if __name__ == '__main__':
    main()
