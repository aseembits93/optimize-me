def sorter(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # Used to detect if a swap occurs
        # Last i elements are already sorted
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Faster swap
                swapped = True
        if not swapped:  # Stop if already sorted
            break
    return arr
