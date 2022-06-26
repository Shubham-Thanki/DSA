from collections import deque


class q:

    def __init__(self) -> None:
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer == 0)

    def size(self):
        return len(self.buffer)


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


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    nums = ['d', 'a', 'f', 'e', 'b', 'c']
    nums_tree = build_tree(nums)
    bfsq = q()
    result = []
    target = 'z'
    contain = False

    # ITERATIVE APPROACH

    bfsq.enqueue(nums_tree)
    # print(bfsq.buffer[0].data)
    while bfsq.size() > 0:
        current = bfsq.dequeue()
        if current.data == target:
            contain = True
        result.append(current)

        if current.left:
            bfsq.enqueue(current.left)
        if current.right:
            bfsq.enqueue(current.right)

for values in result:
    print(values.data, end=',')
print()

print(contain)
