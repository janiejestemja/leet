from lib import add, qsort


def main():
    print("works?")
    print(add(11, 13))

    arr = [x % 7 for x in range(1, 50)]
    print(arr)
    print(qsort(arr))


if __name__ == "__main__":
    main()
