def partition(arr, start, end):
    if start >= end:
        return

    index = start
    pivot = arr[start]
    arr[index], arr[end] = arr[end], arr[index]
    while start < end:
        if(arr[start] < pivot):
            arr[start], arr[index] = arr[index], arr[start]
            index = index + 1
        start = start + 1

    arr[index], arr[end] = arr[end], arr[index]
    # print arr
    print "index ---- {0}".format(index)
    print "arr ---- {0}\n".format(arr)
    return index


def qs(arr, start, end):
    if start >= end:
        return
    index = partition(arr, start, end)
    qs(arr, start, index - 1)
    qs(arr, index + 1, end)
    # print arr


if __name__ == '__main__':
    # print partition([3, 2, 5, 1], 0, 3)
    a = [6, 7, 3, 1, 8, 5]
    qs(a, 0, 5)
    print a
