from core.stack import Stack


class SetOfStack:

    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.stacks = [Stack()]
        self.element_count = 0

    def push(self, data):
        # is stack able to insert in current stacks
        if self.element_count % self.stack_size > 0:
            # just insert in last stack
            self.stacks[-1].add_node(data)
        else:
            # new stack needs to be added
            # add a new stack
            self.stacks.append(Stack())
            # insert in that stack
            self.stacks[-1].add_node(data)

        self.element_count += 1

    def pop(self):
        self.stacks[-1].pop()

    def __str__(self):
        repr = []
        for stack in reversed(self.stacks):
            repr.append(str(stack))
        return "\n-----()-----------()----\n".join(repr)


table = SetOfStack(2)

table.push("notebook")
table.push("mobile")
table.push("thesis")
table.push("ikigayi")

print(table)

table.pop()

print(table)
