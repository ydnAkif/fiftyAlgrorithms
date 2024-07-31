#!/opt/homebrew/bin/python3
# buuble sort algorithm

def bubble_sort(arr):
    last_element_index = len(arr) - 1
    print(0, arr)
    for pass_no in range(last_element_index, 0, -1):
        swapped = False
        for idx in range(pass_no):
            if arr[idx] > arr[idx + 1]:
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
                swapped = True
        if not swapped:
            break
    return arr


if __name__ == '__main__':
    arr_1 = [25, 21, 22, 24, 23, 27, 26]
    sorted_arr = bubble_sort(arr_1)
    sorted(arr_1)
    print(f"Sorted array: {sorted_arr}")
    print(f"Sorted array: {arr_1}")
