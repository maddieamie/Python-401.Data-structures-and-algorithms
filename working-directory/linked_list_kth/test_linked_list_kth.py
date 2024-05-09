import pytest
from linked_list_insertions.linked_list_insertions import LinkedList2, Node2, TargetError
from linked_list_kth.linked_list_kth import kth_from_end

# My tests

def test_kth_from_end_edge_k_equals_length_of_ll():
    new_list = LinkedList2()
    new_list.insert('job')
    new_list.insert('good')
    new_list.insert('you')
    actual = new_list.kth_from_end(2)
    expected = 'you'
    assert actual == expected

def test_kth_from_end_expected_failure_k_not_int():
    e_list = LinkedList2()
    e_list.append('hi')
    with pytest.raises(TargetError):
        e_list.kth_from_end('hi')

def test_kth_from_end_edge_list_linked_is_empty():
    empty_list = LinkedList2()
    with pytest.raises(TargetError):
        empty_list.kth_from_end(2)




# Given tests

# @pytest.mark.skip("TODO")
def test_kth_from_end_zero():
    linked_list = LinkedList2()
    values = ["apples", "bananas", "cucumbers"]
    for value in reversed(values):
        linked_list.insert(value)
    actual = linked_list.kth_from_end(0)
    expected = "cucumbers"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_kth_from_end_one():
    linked_list = LinkedList2()
    values = ["apples", "bananas", "cucumbers"]
    for value in reversed(values):
        linked_list.insert(value)
    actual = linked_list.kth_from_end(1)
    expected = "bananas"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_kth_from_end_two():
    linked_list = LinkedList2()
    values = ["apples", "bananas", "cucumbers"]
    for value in reversed(values):
        linked_list.insert(value)
    actual = linked_list.kth_from_end(2)
    expected = "apples"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_kth_from_end_out_of_range():
    linked_list = LinkedList2()
    values = ["apples", "bananas", "cucumbers"]
    for value in reversed(values):
        linked_list.insert(value)
    with pytest.raises(TargetError):
        linked_list.kth_from_end(3)


# @pytest.mark.skip("TODO")
def test_kth_from_end_under_range():
    linked_list = LinkedList2()
    values = ["apples", "bananas", "cucumbers"]
    for value in reversed(values):
        linked_list.insert(value)
    with pytest.raises(TargetError):
        linked_list.kth_from_end(-1)


# @pytest.mark.skip("TODO")
def test_kth_from_end_size_one():
    linked_list = LinkedList2()
    linked_list.insert("apples")
    actual = linked_list.kth_from_end(0)
    expected = "apples"
    assert actual == expected
