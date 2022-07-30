class Node:
    def __init__(self, data, nextNode):
        self.data = data
        self.nextNode = nextNode


class LinkedList:

    # TODO handle empty case of args
    def __init__(self, *args):
        new_node = Node(args[0], None)
        self.header: Node = new_node
        self.tail: Node = new_node

        if len(args) > 1:
            for arg in args[1:]:
                self.append(arg)

    def add_node(self, node: Node):
        self.tail.nextNode = node
        self.tail = node

    def append(self, data):
        new_node = Node(data, None)
        self.add_node(new_node)

    def __str__(self) -> str:
        print_str = []
        iterator = self.header
        while iterator is not None:
            print_str.append("{} -> ".format(iterator.data))
            iterator = iterator.nextNode
        print_str.append("None")
        return "".join(print_str)

    def __reversed__(self):

        iterator = self.header
        self.tail = iterator
        iterator_next = iterator.nextNode
        iterator.nextNode = None

        prev = iterator
        iterator = iterator_next

        while iterator.nextNode is not None:
            temp = iterator.nextNode
            iterator.nextNode = prev
            prev = iterator
            iterator = temp

        iterator.nextNode = prev
        self.header = iterator
        return self

    def floyd_cycle_method(self) -> bool:
        fast_ptr, slow_ptr = self.header, self.header.nextNode.nextNode
        while slow_ptr is not None:
            if fast_ptr == slow_ptr:
                return True
            else:
                fast_ptr = fast_ptr.nextNode.nextNode
                slow_ptr = slow_ptr.nextNode
        return False
