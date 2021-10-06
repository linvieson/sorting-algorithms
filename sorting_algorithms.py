def selection_sort(arr: list) -> list:
    '''
    Perform selection sort, return sorted array and number of comparisons.
    '''
    comparisons = 0
    length = len(arr)

    if length <= 1:
        return arr, comparisons

    for index in range(length):
        current_min = index

        for index_in_unsorted in range(index + 1, length):
            comparisons += 1

            if arr[current_min] > arr[index_in_unsorted]:
                current_min = index_in_unsorted

        arr[index], arr[current_min] = arr[current_min], arr[index]

    return arr, comparisons


def insertion_sort(arr: list) -> list:
    '''
    Perform insertion sort, return sorted array and number of comparisons.
    '''
    comparisons = 0
    length = len(arr)

    if length <= 1:
        return arr, comparisons

    for index in range(length):

        inner_ind = index
        while (inner_ind > 0) and (arr[inner_ind] < arr[inner_ind - 1]):
            comparisons += 1
            arr[inner_ind], arr[inner_ind - 1] = arr[inner_ind - 1], arr[inner_ind]
            inner_ind -= 1

    return arr, comparisons


def merge_sort(arr: list) -> list:
    '''
    Perform merge sort, return sorted array and number of comparisons.
    '''
    comparisons = 0
    length = len(arr)

    if length <= 1:
        return arr, comparisons

    middle = length // 2
    left, right = arr[:middle], arr[middle:]
    merge_sort(left), merge_sort(right)
    ind_left = ind_right = curr_ind = 0

    while ind_left < len(left) and ind_right < len(right):
        if left[ind_left] < right[ind_right]:
            arr[curr_ind] = left[ind_left]
            ind_left += 1
        else:
            arr[curr_ind] = right[ind_right]
            ind_right += 1

        comparisons += 1
        curr_ind += 1

    while ind_left < len(left):
        arr[curr_ind] = left[ind_left]
        ind_left += 1
        curr_ind += 1

    while ind_right < len(right):
        arr[curr_ind] = right[ind_right]
        ind_right += 1
        curr_ind += 1

    return arr, comparisons


def shellsort(arr: list) -> list:
    '''
    Perform shellsort, return sorted array and number of comparisons.
    '''
    comparisons = 0
    length = len(arr)
    gap = 1

    if length <= 1:
        return arr, comparisons

    gap = 1

    while gap < (length / 3):
        gap = 3 * gap + 1

    while gap >= 1:
        for index in range(gap, length):
            for inner_ind in range(index, gap - 1, -gap):
                comparisons += 1

                if arr[inner_ind] < arr[inner_ind - gap]:
                    arr[inner_ind], arr[inner_ind - gap] = arr[inner_ind - gap], arr[inner_ind]
                else:
                    break

        gap //= 3    

    return  arr, comparisons
