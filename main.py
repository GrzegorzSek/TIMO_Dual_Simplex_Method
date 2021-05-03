# Dual Simplex Method
# max to gradient
# minimum to gradient * (-1)

# Imports
import numpy as np
from prettytable import PrettyTable


def main():
    a = np.array(
        [[0., 1., 1.], [-8., -1., -2.], [-6., -2., -1.], [-5., -1., -1.]])  # wiele rozwiązań na zbiorze ograniczonym
    # a = np.array([[0., 0.5, 1.], [0., -1., 1.], [5., 1., 1.]])    # Tylko jedno rozwiązanie

    dim = 2     # wymiar zadania
    a_dict = {}
    a_dict2 = {}
    a_dict3 = {}
    a_goal = [0, 1, 2]
    a_support = [0, 3, 4, 5]  # zmienne pomocnicze
    rows: int = a.shape[0]  # liczba wierszy
    cols: int = a.shape[1]  # liczba kolumn
    # print(rows, cols)
    step_counter = 1    # liczy kroki - kolejne tabele simpleksowe
    bounded_solution = np.zeros((dim, dim))     # tabela do wyniku wielu rozw. na zbiorze ogr.

    is_a = is_acceptable(cols, a)

    if is_a:
        print('Rozwiązanie jest dualnie dopuszcalne')
        is_b = is_optimal(rows, a)

        while not is_b:
            print('KROK: ' + str(step_counter))
            print('Rozwiązanie jest nieoptymalne')
            row_of_variable_removed_from_base = variable_to_remove(rows, a)  # wiersz zmiennej do usunięcia
            # print('wiersz:' + str(row_of_variable_removed_from_base))
            col_of_variable_added_to_base = variable_to_add(cols, a, row_of_variable_removed_from_base)
            # print('kolumna:' + str(col_of_variable_added_to_base))
            a = gaussian_elimination(a, row_of_variable_removed_from_base, col_of_variable_added_to_base, rows, cols)
            swap_x(a_goal, a_support, row_of_variable_removed_from_base, col_of_variable_added_to_base)

            is_b = is_optimal(rows, a)
            step_counter += 1

            print("macierz wyników")
            # print(a)
            print_solution(a, rows, cols, a_goal, a_support)
            print()

            print("tabele pomocnicze")
            print("f celu: ")
            print(a_goal)
            print("zm pomocnicze: ")
            print(a_support)
            print()

            print("wynik jako dictionary")
            answer_dict(a, a_goal, a_support, a_dict3)
            print(a_dict3)

            print("wynik jako wektor")
            ans3 = []
            answer_array(a_dict3, ans3)
            print(ans3)
            print()

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

        i_s_c = inf_solutions_condition(a, cols)
        if i_s_c:  # Zadanie spełnia warunki na nieskończenie wiele rozwiązań?
            on_limited_set = is_on_limited_set(a, rows, cols)
            on_unlimited_set = is_on_unlimited_set(a, rows, cols)
            if on_limited_set != 0:
                print('A_DICT: ')
                print(a_dict)
                bounded_solution[0, 0] = a_dict[1]
                bounded_solution[0, 1] = a_dict[2]
                for d in range(1, dim):  # pętla, bo musi przeliczyć tyle razy ile ma wymiar zadania
                    print('Zadanie posiada nieskończenie wiele rozwiązań na zbiorze ograniczonym')
                    print()
                    col_no = col_to_opt(a, cols)
                    row_no = row_to_simplex(a, rows, col_no)
                    a = gaussian_elimination(a, row_no, col_no, rows, cols)
                    swap_x(a_goal, a_support, row_no, col_no)

                    # print("macierz wyników")
                    # print(a)
                    # print()
                    #
                    # print("tabele pomocnicze")
                    # print("f celu: ")
                    # print(a_goal)
                    # print("zm pomocnicze: ")
                    # print(a_support)
                    # print()
                    #
                    print("wynik jako dictionary")
                    answer_dict(a, a_goal, a_support, a_dict2)
                    print(a_dict2)

                    print("wynik jako wektor")
                    ans2 = []
                    answer_array(a_dict2, ans2)
                    print(ans2)
                    print()

                    bounded_solution[d, 0] = a_dict2[1]
                    bounded_solution[d, 1] = a_dict2[2]
                print_bounded_solution(bounded_solution)
            elif on_unlimited_set != 0:
                print('Zadanie posiada wiele rozwiązań na zbiorze nieograniczonym')
            else:
                print('Zadanie posiada tylko jedno rozwiązanie')
        else:
            unlimited_task = is_on_unlimited_task(a, rows, cols)
            if unlimited_task:
                print('Zadanie nieograniczone - brak rozwiązań')
            else:
                print('Zadanie posiada tylko jedno rozwiązanie')

    else:
        print('Rozwiązanie nie jest dualnie dopuszczalne')


def print_bounded_solution(bounded_solution):
    dim = bounded_solution.shape[0]
    print('Rozwiązanie zdania dla nieskończenie wielu rozwiązań na zbiorze ograniczonym: ')
    for d in range(0, dim):
        if d < dim - 1:
            print(bounded_solution[d], end="")
            print('*\u03BB' + str(d+1) + ' + ', end="")
        else:
            print(bounded_solution[d], end="")
            print('*\u03BB' + str(d+1))


def print_solution(a, rows, cols, a_goal, a_support):
    s = PrettyTable(['X', str(a_goal)])

    for i in range(0, rows):
        s.add_row([str(a_support[i]), a[0]])
    print(s)


def inf_solutions_condition(a, cols):  # sprawdza czy zadanie spełnia warunki na nieskończenie wiele rozwiązań
    for j in range(1, cols):  # jest to warunek y_0 j >= 0
        if a[0, j] < 0:
            return False
        return True


def is_on_limited_set(a, rows, cols):  # sprawdza czy zadanie posiada nieskończenie wiele rozwiązań na zb. ogr.
    col = 0
    for j in range(1, cols):  # sprawdza czy w wierszu występuje zero - warunek: y_0 j_0 = 0
        if a[0, j] == 0:
            col = j
        else:
            return col

    for i in range(1, rows):  # sprawdza kolejne dwa warunki y_i_0 0 > 0 oraz y_i_0 j_0 >0
        if a[i, 0] > 0:
            if a[i, col] > 0:
                return col
            else:
                col = 0
        else:
            col = 0
    return col


def is_on_unlimited_set(a, rows, cols):  # spradza czy zadanie ma wiele rozw. na zb. nieogr.
    row = 0  # zmienna licząca wiersze z degeneracją
    col = 0
    for j in range(1, cols):  # sprawdza czy w wierszu występuje zero - warunek: y_0 j_0 = 0
        if a[0, j] == 0:
            col = j
        else:
            return col

    for i in range(1, rows):  # sprawdza czy w zadaniu występuje degeneracja - warunek y_i0 = 0 dla i=1, ..., m
        if a[i, 0] == 0:
            row = row + 1

    if row == rows - 1:
        print('Zachodzi degeneracja')
        return col

    for i in range(1, rows):  # sprawdza warunek: y_i j_0 <= 0 dla i=1, ..., m
        if a[i, col] > 0:
            return 0

    return col


def is_on_unlimited_task(a, rows, cols):  # sprawdza czy zadanie jest nieograniczone
    for j in range(0, cols):
        if a[0, j] < 0:
            for i in range(1, rows):
                if a[i, j] > 0:
                    return False
    return True


def answer_dict(a, a_goal, a_support, a_dict):
    for i in range(1, len(a_goal)):
        a_dict[a_goal[i]] = a[0, i]

    for j in range(1, len(a_support)):
        a_dict[a_support[j]] = a[j, 0]


def answer_array(a_dict, ans):
    for i in range(1, len(a_dict) + 1):
        ans.append(a_dict.get(i))


def swap_x(goal, support, row, col):
    temp = goal[col]
    goal[col] = support[row]
    support[row] = temp


def is_acceptable(cols, a):  # test dualnej dopuszczalności zaczyna się od wiersza zerowego
    for j in range(cols):
        if a[0, j] < 0:
            return False
    return True


def is_optimal(rows, a):  # test optymalności zaczyna się od wiersza 1 nie od zerowego
    for i in range(1, rows):
        if a[i, 0] < 0:
            return False
    return True


# def is_multiple_solutions(a, cols):  # sprawdzamy czy f. celu ma zero
#     for i in range(1, cols):
#         if a[0, i] == 0:
#             return True


def col_to_opt(a, cols):  # bierzemy kolumnę, dla której w pierwszym wierszu jest zero
    for j in range(1, cols):
        if a[0, j] == 0:
            return j


def row_to_simplex(a, rows, col):  # szukamy jakie zmienne musimy ze sobą zamienić dla wielu rozw.
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
    print('Usuwamy wiersz: ' + str(row))
    print(x)
    return row


def variable_to_add(cols, a, row):
    new_starting_point = 0
    x = 0
    col = 1

    for j in range(1, cols):  # tutaj bierze pierwszą napotkaną wartość y_0j/y_rj < 0
        if a[row, j] < 0:
            x = a[0, 1] / a[row, j]
            # print(x)
            new_starting_point += 1
            print('Nowy punkt startowy to: ')
            print(new_starting_point)
            break

    for j in range(new_starting_point, cols - 1):
        if a[row, j + 1] < 0 and a[0, j] / a[row, j + 1] > x:
            x = a[0, j] / a[row, j + 1]
            col += 1
    print('Dodajemy kolumnę: ' + str(col))
    print(x)
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
