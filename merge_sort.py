#!/opt/homebrew/bin/python3
# merge sort algorithm


def merge_sort(elements):
    if len(elements) <= 1:
        return elements

    mid = len(elements) // 2
    left = elements[:mid]
    right = elements[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    sorted_list = []
    a = b = 0

    while a < len(left) and b < len(right):
        if left[a] < right[b]:
            sorted_list.append(left[a])
            a += 1
        else:
            sorted_list.append(right[b])
            b += 1

    while a < len(left):
        sorted_list.append(left[a])
        a += 1

    while b < len(right):
        sorted_list.append(right[b])
        b += 1

    return sorted_list


if __name__ == '__main__':
    arr_1 = [25, 21, 22, 24, 23, 27, 26]
    sorted_arr = merge_sort(arr_1)
    print(f"Sorted array: {sorted_arr}")
