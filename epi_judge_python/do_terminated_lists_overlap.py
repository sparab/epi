import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0, l1):
    if not l0 or not l1:
        return None

    counter0 = counter1 = 0
    l = l0
    while l is not None:
        l = l.next
        counter0 += 1

    l = l1
    while l is not None:
        l = l.next
        counter1 += 1

    if counter0 < counter1:
        while counter0 < counter1:
            l1 = l1.next
            counter1 -= 1
    elif counter1 < counter0:
        while counter1 < counter0:
            l0 = l0.next
            counter0 -= 1

    while l0 and l1 and l0 != l1:
        l0, l1 = l0.next, l1.next

    return l0


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(
        functools.partial(overlapping_no_cycle_lists, l0, l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("do_terminated_lists_overlap.py",
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
