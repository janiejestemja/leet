def add(left, right):
    return left + right


def msort(arr):
    if len(arr) == 1:
        return arr

    center = len(arr) // 2
    left, right = arr[:center], arr[center:]

    return merge(msort(left), msort(right))


def merge(left, right):
    i = j = 0

    arr = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1

    arr.extend(left[i:])
    arr.extend(right[j:])

    return arr



def qsort(arr):
    if len(arr) <= 1:
        return arr
    pivot = len(arr) // 2
    l = [x for x in arr if x < arr[pivot]]
    c = [x for x in arr if x == arr[pivot]]
    r = [x for x in arr if x > arr[pivot]]
    return qsort(l) + c + qsort(r)


def search(arr, tar):
    lower = 0
    upper = int(len(arr)) - 1

    if tar > arr[-1]:
        lower = upper

    while lower <= upper:
        center = (lower + upper) // 2

        if arr[center] == tar:
            return center
        elif arr[center] < tar:
            lower += 1
        else:
            upper -= 1

    return lower
