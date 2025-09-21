from lib import add, qsort, search, msort
from list_lib import Node
from tree_lib import Tree


def main():
    print("works?")
    print(add(11, 13))

    print(medSlideArr([1,3,-1,-3,5,3,6,7], 3))
    print(get_medians([1,3,-1,-3,5,3,6,7], 3))
    print(medSlideArr([1,4,2,3], 4))
    print(get_medians([1,4,2,3], 4))


    arr = [1,3,-1,-3,5,3,6,7]
    arr = [(-1)**(i % 3) * (x % 11) for i, x in enumerate(range(-22, 23))]
    k = 3
    print(arr)
    print(get_medians(arr, k))


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

def longest_unique(seq):
    cmap = {}
    istart = 0
    longest = ""

    for i, ele in enumerate(seq):
        if ele in cmap and istart <= cmap[ele]:
            istart = cmap[ele] + 1

        cmap[ele] = i
        current = seq[istart: i + 1]

        if len(current) > len(longest):
            longest = current

    return longest


def circle_main():
    arr = [(-1)**(i % 3) * (x % 11) for i, x in enumerate(range(-22, 23))]
    print(arr)
    node = Node.from_arr(arr)

    circle = make_circle(node, 5)

    print(Node.check_circle(node))
    print(Node.check_circle(circle))


def make_circle(node, index):
    start = Node(None, None)
    tail = start

    counter = 0
    circlepoint = None
    while node:
        if counter == index:
            tail.next = node
            circlepoint = tail
            node = node.next
        else:
            tail.next = node
            node = node.next
        counter += 1
    tail.next = circlepoint

    return start.next


def qsearch_main():
    arr = [(-1)**(i % 3) * (x % 11) for i, x in enumerate(range(-22, 23))]
    qsort_arr = qsort(arr)
    msort_arr = msort(arr)
    assert(qsort_arr == msort_arr)

    mindex = search(qsort_arr, 0)
    qindex = search(msort_arr, 0)
    assert(qindex == mindex)

    print(arr)
    print(qsort_arr)
    print(msort_arr)
    print(mindex)
    print(qindex)

    # for matrix
    mat = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    tar = 5
    tara = 0
    mat = [[-1], [1]]
    mat = [[1, 3, 5]]
    tara = 4

    x = qsearch(mat, tar)
    print(x)
    x = qsearch(mat, tara)
    print(x)

# Searching a very sorted 2D matrix
def qsearch(mat, tar):
    if not mat or not mat[0]:
        return False

    row, col = 0, len(mat[0]) - 1

    while row < len(mat) and 0 <= col:
        cur = mat[row][col]
        if cur == tar:
            return True
        elif cur > tar:
            col -= 1
        else:
            row += 1

    return False

if __name__ == "__main__":
    main()
