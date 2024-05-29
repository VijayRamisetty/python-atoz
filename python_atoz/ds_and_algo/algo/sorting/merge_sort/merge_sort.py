def merge_sort_sorted_arrays(a, b):
    len_a = len(a)
    len_b = len(b)
    i = j = 0
    sorted_list = []
    while i < len_a and j < len_b:
        if a[i] < b[j]:
            sorted_list.append(a[i])
            i = i+1
        else:
            sorted_list.append(b[j])
            j = j+1

    # handle left over from both a and b if any
    while i < len_a:
        sorted_list.append(a[i])
        i = i + 1
    while j < len_b:
        sorted_list.append(b[j])
        j = j + 1

    return sorted_list


if __name__ == '__main__':
    """
    given two sorted arrays, write code for merge sort
    """

    a = [10, 23, 45, 51, 68]
    b = [11, 33, 29, 48]

    result = merge_sort_sorted_arrays(a, b)
    print(result)
