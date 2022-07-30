
def rotate_swap(arr, row, col):
    array_last_index = len(arr) - 1

    arr[row][col], arr[array_last_index - col][row], arr[array_last_index - row][array_last_index-col], arr[col][array_last_index - row] = \
        arr[array_last_index - col][row], arr[array_last_index - row][array_last_index-col], arr[col][array_last_index - row], arr[row][col]




def rotate(arr):
    N = len(arr)
    rows = N // 2
    for row in range(rows):
        max_cols = N  - (row + 1)
        for col in range(row, max_cols):
            print(row, col)
            rotate_swap(arr, row, col)


arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

arr_rotated = [
    [3, 6, 9],
    [2, 5, 8],
    [1, 4, 7]
]

test_array_elements(arr1, arr2)
print(rotate(arr) == arr_rotated)
print(arr)

