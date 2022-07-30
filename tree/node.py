
class single_node:

    def __init__(self, data):
        self.data = data
        self.next = None


class double_node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class tree_node:

    def __init__(self, data):
        self.val = data
        self.left:tree_node = None
        self.right:tree_node = None

