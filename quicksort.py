def quick_sort(arr, start=0, end=None):
    if end is None:
        end = len(arr) - 1
    
    if start < end:
        pivot_index = partition(arr, start, end)
        quick_sort(arr, start, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, end)
    return arr
