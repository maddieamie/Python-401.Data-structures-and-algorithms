import pytest
from linked_list_zip.linked_list_zip import zip_lists
from linked_list_insertions.linked_list_insertions import LinkedList2, Node2, TargetError

# Tests written by me
def test_improper_argument_2_string():
    list1 = LinkedList2()
    with pytest.raises(TargetError):
        zip_lists(list1, 'hi')


def test_improper_argument_1_int():
    list1 = LinkedList2()
    with pytest.raises(TargetError):
        zip_lists(1, list1)


def test_alternate_node_types():
    dictionary = {1: "yay"}
    extralist = ['list', 'thing', 3]
    list1 = LinkedList2()
    list1.append('hi')
    list1.append(dictionary)
    list1.append(extralist)

    def new():
        return 'blah'
    floatnum = 9.333444555
    list2 = LinkedList2()
    list2.append('bye')
    list2.append(new())
    list2.append(floatnum)

    assert zip_lists(list1, list2)


# Tests provided by Code Fellows
def test_exists():
    assert zip_lists


# @pytest.mark.skip("TODO")
def test_even_length():
    list_a = LinkedList2()
    for value in reversed([1, 2, 3]):
        list_a.insert(value)

    list_b = LinkedList2()
    for value in reversed(["a", "b", "c"]):
        list_b.insert(value)

    actual = zip_lists(list_a, list_b)
    expected = LinkedList2()
    for value in reversed([1, "a", 2, "b", 3, "c"]):
        expected.insert(value)

    assert str(actual) == str(expected)


# @pytest.mark.skip("TODO")
def test_a_shorter():
    list_a = LinkedList2()
    for value in reversed([1, 2]):
        list_a.insert(value)

    list_b = LinkedList2()
    for value in reversed(["a", "b", "c"]):
        list_b.insert(value)

    actual = zip_lists(list_a, list_b)
    expected = LinkedList2()
    for value in reversed([1, "a", 2, "b", "c"]):
        expected.insert(value)

    assert str(actual) == str(expected)


# @pytest.mark.skip("TODO")
def test_b_shorter():
    list_a = LinkedList2()
    for value in reversed([1, 2, 3]):
        list_a.insert(value)

    list_b = LinkedList2()
    for value in reversed(["a", "b"]):
        list_b.insert(value)

    actual = zip_lists(list_a, list_b)
    expected = LinkedList2()
    for value in reversed([1, "a", 2, "b", 3]):
        expected.insert(value)

    assert str(actual) == str(expected)


# @pytest.mark.skip("TODO")
def test_a_empty():
    list_a = LinkedList2()
    list_b = LinkedList2()
    for value in reversed(["a", "b", "c"]):
        list_b.insert(value)

    actual = zip_lists(list_a, list_b)
    expected = LinkedList2()
    for value in reversed(["a", "b", "c"]):
        expected.insert(value)
    assert str(actual) == str(expected)


# @pytest.mark.skip("TODO")
def test_b_empty():
    list_a = LinkedList2()
    for value in reversed([1, 2, 3]):
        list_a.insert(value)
    list_b = LinkedList2()
    actual = zip_lists(list_a, list_b)
    expected = LinkedList2()
    for value in reversed([1, 2, 3]):
        expected.insert(value)
    assert str(actual) == str(expected)
