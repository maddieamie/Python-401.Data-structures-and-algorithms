from tree_max.binary_tree import BinaryTree, Node


class Max(BinaryTree):
    def find_maximum_value(self, start=None):
        if start is None:
            node = self.root
        else:
            node = start

        if not self.root:
            return None

        max = node.value

        # if node.value > max:
        #     max = node.value

        if node.left:
            left = self.find_maximum_value(node.left)
            if max < left:
                max = left
        if node.right:
            right = self.find_maximum_value(node.right)
            if max < right:
                max = right

        return max


