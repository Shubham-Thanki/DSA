# import numbers


class BinarySearchTreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            # Add data to the left sub tree
            if self.left:  # If the selected node is not empty
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # Add data to the right sub tree
            if self.right:  # If the selected node has some elements on the right
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []
        # Visit the left tree
        if self.left:
            # print(elements)
            elements += self.left.in_order_traversal()

        # Visit the node
        elements.append(self.data)

        # Visit the right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        elements = []

        # Visit the node
        elements.append(self.data)

        # Visit the left tree
        if self.left:
            elements += self.left.pre_order_traversal()

        # Visit the right tree
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    num = [12, 56, 1, 68, 54, 23, 38]
    num_tree = build_tree(num)
    # print(num_tree, 'oko')
    print(num_tree.pre_order_traversal())
