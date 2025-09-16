def add(left, right):
    return left + right


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
    upper = int(len(arr) / 2)

    while lower <= upper:
        center = (lower + upper) // 2

        if tar == arr[center]:
            return center
        elif tar > arr[center]:
            lower += 1
        else:
            upper -= 1

    return lower
