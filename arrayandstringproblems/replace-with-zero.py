


"""

Q) Given a m x n matrix, if an element is 0, set its entire row and column to 0.
Input =
[
[1, 1, 1],
[1, 0 ,1],
[1, 1, 1]
]
output =
[
[1, 0, 1],
[0, 0 ,0],
[1, 0, 1]
]
"""


def replace_with_zero(arr):

    rows_to_zero = set()
    col_to_zero = set()


    for row_index, row in enumerate(arr):

        for col_index, column in enumerate(row):

            if arr[row_index][col_index] == 0:
                rows_to_zero.add(row_index)
                col_to_zero.add(col_index)

    row_length = len(arr)
    col_length = len(arr[0])

    for row_to_zero_row in rows_to_zero:
        for col_index in range(col_length):
            print("setting row", row_to_zero_row, col_index)
            arr[row_to_zero_row][col_index] = 0


    for col_to_zero_col in col_to_zero:
        for row_index in range(row_length):
            print("setting col", col_to_zero_col, row_index)
            arr[row_index][col_to_zero_col] = 0

    print(arr)
    return arr

def test_replace_with_zero():
    a = replace_with_zero(
    [
    [1, 1, 1],
    [1, 0 ,1],
    [1, 1, 1]
    ])

    print(a[1][0] == a[0][1] == a[1][1] == a[1][2] == a[2][1] == 0)

def test_replace_with_zero_input2():
    a = replace_with_zero(
        [
            [1, 0, 1, 0],
            [1, 1, 1, 1],
            [1, 1, 1, 1]
        ]
    )

    print(a)


test_replace_with_zero()
test_replace_with_zero_input2()
