def sorter(arr: list[int] | list[float]) -> list[int] | list[float]:
    # Use Python's highly optimized in-place sort for much better performance
    arr.sort()
    return arr
