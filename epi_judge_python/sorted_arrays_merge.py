from test_framework import generic_test
import heapq


def merge_sorted_arrays(sorted_arrays):
    min_heap = []

    sorted_arrays_iter = [iter(x) for x in sorted_arrays ]

    for i, it in enumerate(sorted_arrays_iter):
        first_element = next(it, None)
        if first_element is not None:
            heapq.heappush(min_heap, (first_element, i))

    result = []
    while min_heap:
        element = heapq.heappop(min_heap)
        result.append(element[0])
        next_element = next(sorted_arrays_iter[element[1]], None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, element[1]))

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
