'''
binary tree

https://www.cs.cmu.edu/~adamchik/15-121/lectures/Trees/trees.html

'''

from node import tree_node


class tree:

    def __init__(self, data):
        self.root : tree_node = tree_node(data)


    def add(self, data):
        self.insert(self.root, data)


    def preorder(self):
        self.print_pre(self.root)


    def postorder(self):
        self.print_post(self.root)


    def inorder(self):
        self.print_inorder(self.root)


    def levelorder(self):
        self.print_levelorder(self.root)



    def insert(self, node : tree_node, data):
            if node.val > data:
                if node.left == None:
                    node.left = tree_node(data)
                else:
                    self.insert(node.left, data)
            else:
                if node.right == None:
                    node.right = tree_node(data)
                else:
                    self.insert(node.right, data)
    

    # left root right
    def print_inorder(self, node : tree_node):
        if node == None:
            return
        else:
            self.print_inorder(node.left)
            print(node.val)
            self.print_inorder(node.right)


    def print_pre(self, node : tree_node):
        if node == None:
            return
        else:
            print(node.val)
            self.print_inorder(node.left)
            self.print_inorder(node.right)


    def print_post(self, node : tree_node):
        if node == None:
            return
        else:
            self.print_inorder(node.left)
            self.print_inorder(node.right)
            print(node.val)


    def print_levelorder(self, node):
        '''
        +
        \  \ 
        -   +
        \ \  \ \
        1 2  3 4

        + - + 1 2 3 4

        '''





if __name__ == '__main__':

    bst = tree("5")

    for var in "1 4 7 2 6 9".split():
        bst.add(var)

    print("inorder")
    bst.inorder()

    print("preorder")
    bst.preorder()

    print("postorder")
    bst.postorder()
