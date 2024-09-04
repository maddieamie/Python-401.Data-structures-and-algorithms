class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root_value=None):
        self.root = Node(root_value)

    def insert(self, parent_value, child_value, is_left=True):
        parent_node = self._find(self.root, parent_value)
        if parent_node:
            if is_left:
                parent_node.left = Node(child_value)
            else:
                parent_node.right = Node(child_value)

    def _find(self, node, value):
        if node is None:
            return None
        if node.value == value:
            return node
        left_result = self._find(node.left, value)
        if left_result:
            return left_result
        return self._find(node.right, value)

    def in_order_traversal(self):
        return self._in_order_traversal_recursive(self.root)

    def _in_order_traversal_recursive(self, node):
        elements = []
        if node.left:
            elements += self._in_order_traversal_recursive(node.left)
        elements.append(node.value)
        if node.right:
            elements += self._in_order_traversal_recursive(node.right)
        return elements
