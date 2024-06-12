def heap_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    # Convert the array into a heap.
    heapify(arr)

    n = len(arr)

    # Move the root of the heap to the end of the array
    # and then "heapify" the remaining elements.
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap root with the last element.
        bubble_down(arr, 0, i)  # Heapify the remaining heap.

    return arr


def heapify(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        bubble_down(arr, i, n)

    # O(n) time.
    # O(1) auxiliary space.
    # O(n) total space.


def bubble_down(arr, i, n):
    curr_index = i
    # left_child_idx = 2 * curr_index + 1

    while (2 * curr_index + 1) < n:
        # Find the smaller child.
        smallest_child_index = 2 * curr_index + 1
        right_child_idx = 2 * curr_index + 2

        if right_child_idx < n and -arr[right_child_idx] < -arr[smallest_child_index]:
            smallest_child_index = right_child_idx

        # Check if the heap property is achieved.
        if -arr[curr_index] < -arr[smallest_child_index]:
            break
        # Swap elements to maintain heap property.
        else:
            arr[curr_index], arr[smallest_child_index] = (
                arr[smallest_child_index],
                arr[curr_index],
            )
            curr_index = smallest_child_index

    # O(log n) time.
    # O(1) auxiliary space.
    # O(n) total space.


lst = [1, 23, -23, -1]
print(heap_sort(lst))  # -> [-23, -1, 1, 23]
