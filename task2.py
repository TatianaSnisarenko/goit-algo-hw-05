def binary_search(arr, x):
    iterations = 0

    if not arr or not x or arr[len(arr) - 1] < x:
        return (iterations, None)
    low = 0
    high = len(arr) - 1
    mid = 0
    up_bnd_inx = high

    while low <= high:
        iterations += 1
        mid = (high + low) // 2
        if arr[mid] == x:
            return (iterations, arr[mid])
        elif arr[mid] < x:
            up_bnd_inx = high if arr[high] < arr[up_bnd_inx] and arr[high] > x else up_bnd_inx
            low = mid + 1
        elif arr[mid] > x:
            up_bnd_inx = mid - 1 if arr[mid - 1] > x and mid - 1 >= 0 else mid
            high = mid - 1

    return (iterations, arr[up_bnd_inx])
