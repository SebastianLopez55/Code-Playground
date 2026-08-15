def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[len(array) // 2]
    smaller = [smaller for smaller in array if smaller < pivot]
    equal = [mid for mid in array if mid == pivot]
    greater = [greater for greater in array if greater > pivot]

    return quick_sort(smaller) + equal + quick_sort(greater)


lst = [1, 2, 33, 2]
print(quick_sort(lst))
