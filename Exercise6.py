import Exercise5

ar = [
    [1, 4, 7, 2, 5],
    [5, 8, 5, 3, 1],
    [2, 4, 7, 8, 1],
    [1, 3, 4, 2, 6],
    [1, 7, 4, 2, 1]
]


def sort_by_row(array):
    for rows in range(len(array)):
        Exercise5.bubble_sort(array[rows])

def sort_by_col(array):
    for i in range(len(array)):
        col_list = []
        for j in range(len(array)):
            col_list.append(array[j][i])
        Exercise5.bubble_sort(col_list)
        for j in range(len(array)):
            array[j][i] = col_list[j]
sort_by_row(ar)
print(ar)
sort_by_col(ar)
print(ar)

