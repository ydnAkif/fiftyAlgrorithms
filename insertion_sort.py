#!/opt/homebrew/bin/python3
# insertion sort algorithm

def insertion_sort(elements):
    for i in range(1, len(elements)):
        j = i - 1
        next_element = elements[i]
        while j >= 0 and elements[j] > next_element:
            elements[j + 1] = elements[j]
            j -= 1
        elements[j + 1] = next_element

    return elements


if __name__ == '__main__':
    arr_1 = [25, 21, 22, 24, 23, 27, 26]
    sorted_arr = insertion_sort(arr_1)
    print(f"Sorted array: {sorted_arr}")
