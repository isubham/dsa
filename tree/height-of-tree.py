from node import tree_node


class HeightOfTree:

    def __init__(self, bfs_nodes) -> None:
        self.bfs_nodes = bfs_nodes

    def print_pre(self, node):
        if node is None:
            return
        else:
            print(node.val)
            self.print_pre(node.left)
            self.print_pre(node.right)

    def insert_bfs(self, bfs_nodes, pos):
        """
        [1, 2, 4, null, null, 5, 6]
                    1 (0)
            2 (1)               4 (2)
        null (3)    null (4)    5 (5)       6 (5)
        """
        print('inserting bfs for index', pos)
        val = bfs_nodes[pos]
        a_tree_node = tree_node(val)
        if val is not None:

            if pos == 0:
                self.root = a_tree_node

            left_node_index = 2 * pos + 1
            right_node_index = 2 * pos + 2

            if left_node_index < len(bfs_nodes):
                print('assigning left')
                a_tree_node.left = self.insert_bfs(bfs_nodes, left_node_index)

            if right_node_index < len(bfs_nodes):
                a_tree_node.right = self.insert_bfs(bfs_nodes, right_node_index)

        return a_tree_node

    def height_of_tree(bfs_nodes) -> None:
        """
                    1 (2)
            2 (1) (0)               4 (2) (1)
        null (3) (0)    null (4)(0)    5 (5)(0)       6 (5)(0)
        """


    def labelHeight(self, node, height_diff):
        if (node == None):
            return 0
        elif node.left is None and node.right is None:
            print('node is at leaf', node.val)
            node.height = 0
            return 0

        elif node.left is not None:
            print('node', node.val)
            print('going to assign left', node.left.val)
            self.labelHeight(node.left, height_diff)

        elif root.right is not None:
            print('node right', node.right.val)
            self.labelHeight(node.right, height_diff)

        # assign root height to max of left and right
        left_height = node.left.height + 1 if hasattr(node.left, "height") else 0
        right_height = node.right.height + 1 if hasattr(node.right, "height") else 0
        node.height = max(left_height, right_height)

        # assign heightDiff
        current_height_diff = abs(left_height - right_height)
        if (height_diff < current_height_diff):
            height_diff = current_height_diff

        return height_diff


    def isBalanced(self, root):
        heightDiff = self.labelHeight(root, 0)
        return heightDiff > 1



if __name__ == '__main__':
    hot_instance = HeightOfTree([1, 2, 4, None, None, 5, 6])
    print(hot_instance)
    root = hot_instance.insert_bfs(hot_instance.bfs_nodes, 0)
    # hot_instance.print_pre(root)
    hot_instance.isBalanced(root)


