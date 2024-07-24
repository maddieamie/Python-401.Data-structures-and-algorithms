import pytest
from linked_list_insertions.linked_list_insertions import LinkedList2, TargetError



# @pytest.mark.skip("TODO")
def test_append():
    linked_list = LinkedList2()

    linked_list.insert("apple")

    linked_list.insert("banana")

    linked_list.append("cucumber")

    assert str(linked_list) == "banana -> apple -> cucumber -> Null"


# @pytest.mark.skip("TODO")
def test_insert_before():
    linked_list = LinkedList2()

    linked_list.insert("apple")

    linked_list.insert("banana")

    linked_list.insert_before("apple", "cucumber")

    assert str(linked_list) == "banana -> cucumber -> apple -> Null"


# @pytest.mark.skip("TODO")
def test_insert_before_first():
    linked_list = LinkedList2()

    linked_list.insert("apple")

    linked_list.insert_before("apple", "cucumber")

    assert str(linked_list) == "cucumber -> apple -> Null"


#@pytest.mark.skip("TODO")
def test_insert_after():
    linked_list = LinkedList2()

    linked_list.insert("apple")

    linked_list.insert("banana")

    linked_list.insert_after("banana", "cucumber")

    assert str(linked_list) == "banana -> cucumber -> apple -> Null"


# @pytest.mark.skip("TODO")
def test_insert_before_empty():
    linked_list = LinkedList2()

    with pytest.raises(TargetError):
        linked_list.insert_before("radish", "zucchinni")


# @pytest.mark.skip("TODO")
def test_insert_before_missing():
    linked_list = LinkedList2()

    linked_list.insert("banana")

    with pytest.raises(TargetError):
        linked_list.insert_before("radish", "zucchinni")


# @pytest.mark.skip("TODO")
def test_insert_after_empty():
    linked_list = LinkedList2()

    with pytest.raises(TargetError):
        linked_list.insert_after("radish", "zucchinni")


# @pytest.mark.skip("TODO")
def test_insert_after_missing():
    linked_list = LinkedList2()

    linked_list.insert("banana")

    with pytest.raises(TargetError):
        linked_list.insert_after("radish", "zucchinni")


def test_happy_path_append():
    new_list = LinkedList2()
    new_list.insert('job')
    new_list.insert('good')
    new_list.append('you')
    assert str(new_list) == 'good -> job -> you -> Null'


def test_happy_path_append_empty():
    empty_list = LinkedList2()
    empty_list.append('hi')
    expected_output = 'hi -> Null'
    assert str(empty_list) == expected_output
