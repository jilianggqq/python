
def bs(arr, key, start, end):
    if end < start:
        return -1
    m = (start + end) / 2
    # print m
    if key == arr[m]:
        return m
    elif key < arr[m]:
        # search left
        return bs(arr, key, start, m - 1)
    else:
        # search right
        return bs(arr, key, m + 1, end)

if __name__ == '__main__':
    index = bs([1, 2, 2.4, 3, 4], 2.5, 0, 3)
    print index
