import pytest
from pseudo_queue.pseudo_queue import PseudoQueue


def test_exists():
    assert PseudoQueue


# @pytest.mark.skip("TODO")
def test_enqueue_one():
    pq = PseudoQueue()
    pq.enqueue("apples")
    actual = pq.dequeue()
    expected = 'apples'
    assert str(actual) == expected


# @pytest.mark.skip("TODO")
def test_enqueue_two():
    pq = PseudoQueue()
    pq.enqueue("apples")
    pq.enqueue("bananas")

    actual = pq.dequeue()
    expected = "apples"
    assert str(actual) == expected

    actual = pq.dequeue()
    expected = "bananas"
    assert str(actual) == expected


# @pytest.mark.skip("TODO")
def test_enqueue_dequeue_enqueue_dequeue():
    pq = PseudoQueue()
    pq.enqueue("apples")
    pq.enqueue("bananas")

    pq.dequeue()

    pq.enqueue("cucumbers")
    pq.enqueue("dates")

    actual = [pq.dequeue(), pq.dequeue(), pq.dequeue()]

    expected = ["bananas", "cucumbers", "dates"]

    assert actual == expected

# @pytest.mark.skip("TODO")
def test_empty():
    pq = PseudoQueue()
    with pytest.raises(Exception):
        pq.dequeue()

# @pytest.mark.skip("TODO")
def test_hidden_stacks():
    pq = PseudoQueue()
    pq.enqueue("apples")
    pq.enqueue("bananas")

    assert str(pq.pseudo_queue) == "apples -> bananas"
    assert str(pq.stack_2) == ""
    assert str(pq.stack_1) == ""
