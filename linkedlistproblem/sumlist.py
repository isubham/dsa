"""
CTCI

Sum list
21 Aug 2021

"""

from core.linkedlist import LinkedList, Node


def sum_list(digits_a: LinkedList, digits_b: LinkedList) -> LinkedList:
    """
    :param digits_a: 196 represented as 6 -> 9 -> 1
    :param digits_b: 76 represented as 6 -> 9
    :return: sum   272 represented as 2 -> 7 -> 2
    """

    num_a_iter: Node = digits_a.header
    num_b_iter: Node = digits_b.header
    sum_ab = LinkedList(0)
    iter_count = 0
    carry = 0
    while num_a_iter is not None or num_b_iter is not None:

        place_sum = 0
        if num_a_iter is not None and num_b_iter is not None:
            carry, place_sum = divmod(num_a_iter.val + num_b_iter.val + carry, 10)
            num_b_iter = num_b_iter.nextNode
            num_a_iter = num_a_iter.nextNode

        elif num_a_iter is not None and num_b_iter is None:
            carry, place_sum = divmod(num_a_iter.val + carry, 10)
            num_a_iter = num_a_iter.nextNode

        elif num_a_iter is None and num_b_iter is not None:
            carry, place_sum = divmod(num_b_iter.val + carry, 10)
            num_b_iter = num_b_iter.nextNode

        if iter_count == 0:
            sum_ab.header.val = place_sum
            iter_count += 1
        else:
            sum_ab.append(place_sum)

    return sum_ab


print(sum_list(LinkedList(6, 2), LinkedList(7, 9, 1)))
