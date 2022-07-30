class StackNode:
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node


class Stack:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        if self.head == None:
            new_node = StackNode(data, None)
            self.head = new_node
        else:
            new_node = StackNode(data, self.head)
            self.head = new_node

    def pop(self):
        item_to_delete = self.head
        self.head = self.head.next_node
        del item_to_delete

    def __str__(self):
        iterator = self.head
        repr = []
        max_length_data = 0
        while iterator is not None:

            if (max_length_data < len(iterator.val)):
                max_length_data = len(iterator.val)

            repr.append("{}".format(iterator.val))
            iterator = iterator.next_node

        return "\n{}\n".format("-" * max_length_data).join(repr)

    def is_empty(self) -> bool:
        return self.head is None
