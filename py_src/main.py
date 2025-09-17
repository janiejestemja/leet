from lib import add, qsort, search, msort


def main():
    print("works?")
    print(add(11, 13))

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


if __name__ == "__main__":
    main()
