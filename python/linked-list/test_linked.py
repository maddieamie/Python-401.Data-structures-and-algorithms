import pytest
from linked import Node, LinkedList


def test_node_1():
    actual = Node(34).value
    expected = 34
    assert actual == expected


def test_node_2():
    actual = Node(35).next
    expected = None
    assert actual == expected


def test_linked_list_to_string_1():
    list2 = LinkedList()
    actual = list2.to_string()
    expected = "Null"
    assert actual == expected


def test_linked_list_instantiate():
    list_blank = LinkedList()
    actual = list_blank.head
    expected = None
    assert actual == expected


def test_insert_test_1():
    list1 = LinkedList()
    actual = list1.insert(33)
    expected = list1.head.value
    assert actual == expected


def test_insert_test_head_2():
    list2 = LinkedList()
    list2.insert(1)
    list2.insert(2)
    actual = list2.insert(3)
    expected = list2.head.value
    assert actual == expected


def test_includes_test_value_true():
    list3 = LinkedList()
    list3.insert(15)
    list3.insert(12)
    list3.insert(16)
    actual = list3.includes(12)
    expected = True
    assert actual == expected


def test_includes_test_value_false():
    list4 = LinkedList()
    list4.insert(11)
    list4.insert(10)
    list4.insert(9)
    actual = list4.includes(13)
    expected = False
    assert actual == expected


def test_to_string():
    new_linked = LinkedList()
    new_linked.insert(666)
    new_linked.insert(777)
    new_linked.insert(999)
    actual = new_linked.to_string()
    expected = ' 999 -> 777 -> 666 ->Null'
    assert actual == expected
