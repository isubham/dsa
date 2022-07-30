
from core.linkedlist import LinkedList
from linkedlistproblem.sumlist import sum_list


def sum_list_reverse(digits_a: LinkedList, digits_b: LinkedList) -> LinkedList:
    """
    :param digits_a:196 represented as 1 -> 9 -> 6
    :param digits_b: 76 represented as 7 -> 6
    :return: sum    272 represented as 2 -> 7 -> 2
    """
    # reverse the list and then use the previous method
    digits_a_reversed = reversed(digits_a)
    digits_b_reversed = reversed(digits_b)
    result = sum_list(digits_a_reversed, digits_b_reversed)
    return result


print(sum_list_reverse(LinkedList(1, 9, 6), LinkedList(7, 6)))
# reverse the array and use the sum_list function


