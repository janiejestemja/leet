def add(left, right):
    return left + right

def get_medians(arr, k):
    slider = Slider(arr[:k])
    i = 0
    meds = []
    meds.append(slider.getMed())
    while i + k < len(arr):
        slider.move_window(arr[i], arr[k + i])
        i += 1
        meds.append(slider.getMed())

    return meds


# Naive implementation.
def medSlideArr(arr, k):
    i, j = 0, k
    kh = k // 2

    res = []
    while j <= len(arr):
        widow = arr[i:j]
        widow.sort()
        if k % 2 == 0:
            med = (widow[kh-1] + widow[kh]) / 2
            res.append(med)
        else:
            med = widow[kh]
            res.append(med)

        i += 1
        j += 1

    return res


class Slider:
    def __init__(self, arr):
        self.window = self.mersort(arr)

    def move_window(self, prev, next):
        self.window.remove(prev)
        tari = self.binsearch(self.window, next)
        self.window.insert(tari, next)

    def getMed(self):
        length = len(self.window)
        if length % 2 == 0:
            return (self.window[length//2 - 1] + self.window[length//2]) / 2
        else:
            return self.window[length//2]

    @classmethod
    def mersort(cls, arr):
        if len(arr) <= 1:
            return arr

        piv = len(arr) // 2
        left, right = arr[:piv], arr[piv:]
        left = cls.mersort(left)
        right = cls.mersort(right)
        return cls.merges(left, right)

    @classmethod
    def merges(cls, left, right):
        i, j = 0, 0

        sorted = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                sorted.append(left[i])
                i += 1
            else:
                sorted.append(right[j])
                j += 1

        sorted.extend(left[i:])
        sorted.extend(right[j:])

        return sorted

    def binsearch(self, arr, tar):
        i, j = 0, len(arr)

        while i < j:
            center = (i + j) // 2

            if arr[center] == tar:
                return center
            elif arr[center] < tar:
                i += 1
            else:
                j -= 1

        return i



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
