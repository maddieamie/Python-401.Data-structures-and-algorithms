import pytest
from tree_max.binary_tree import Node

from tree_max.tree_max import Max

# @pytest.mark.skip("TODO")
def test_max_val():
    tree = Max()
    tree.root = Node(10)
    tree.root.left = Node(30)
    tree.root.right = Node(-7)
    actual = tree.find_maximum_value()
    expected = 30

    assert actual == expected


def test_custom_tree():
    tree = Max(2)

    tree.insert(2, 7, is_left=True)            # root.left = 7
    tree.insert(7, 2, is_left=True)            # root.left.left = 2
    tree.insert(7, 6, is_left=False)           # root.left.right = 6
    tree.insert(6, 5, is_left=True)            # root.left.right.left = 5
    tree.insert(6, 11, is_left=False)          # root.left.right.right = 11
    tree.insert(2, 5, is_left=False)           # root.right = 5
    tree.insert(5, 9, is_left=False)           # root.right.right = 9
    tree.insert(9, 4, is_left=True)            # root.right.right.left = 4

    actual = tree.find_maximum_value()
    expected = 11

    assert actual == expected


def test_custom_tree_2():
    tree = Max(11)

    tree.insert(11, 0, is_left=True)            # root.left = 0
    tree.insert(0, 13, is_left=False)           # root.left.right = 13
    tree.insert(11, 12, is_left=False)          # root.right = 12
    tree.insert(12, 2, is_left=True)            # root.right.left = 2

    actual = tree.find_maximum_value()
    expected = 13

    assert actual == expected


def test_custom_tree_3():
    tree = Max(2)

    tree.insert(2, 7, is_left=True)  # root.left = 7
    tree.insert(2, 10, is_left=False) # root.right = 10

    actual = tree.find_maximum_value()
    expected = 10

    assert actual == expected


def test_tree_empty():
    tree = Max()
    actual = tree.find_maximum_value()
    expected = None

    assert actual == expected


def test_tree_only_root():
    tree = Max(10)
    actual = tree.find_maximum_value()
    expected = 10

    assert actual == expected



