"""
25th August 2020

Cycle detection with Floyd Cycle Detection

"""

from core.linkedlist import LinkedList, Node




def main():
    cycle_node = Node(33, Node)
    cycle_ll = LinkedList(1, 2, 5)
    print(cycle_ll.floyd_cycle_method() == False)
    cycle_ll.add_node(cycle_node)
    cycle_ll.tail.nextNode = cycle_ll.header.nextNode
    print(cycle_ll.floyd_cycle_method() == True)


main()
