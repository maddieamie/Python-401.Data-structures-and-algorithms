import pytest
from stacks_and_queues.queue import Queue


def test_exists():
    assert Queue


def test_queue_is_empty():
    ss = Queue()
    assert ss.is_empty() is True


def test_queue_is_empty_false():
    s = Queue()
    s.enqueue('brrrrr')
    assert s.is_empty() is False


def test_dequeue_on_empty_queue():
    p = Queue()
    with pytest.raises(Exception):
        p.dequeue()


def test_peek_on_empty_queue():
    n = Queue()
    with pytest.raises(Exception):
        n.peek()


# @pytest.mark.skip("TODO")
def test_peek_return():
    pab = Queue()
    pab.enqueue("peek")
    pab.enqueue("a")
    pab.enqueue("boo")
    assert pab.peek() == "peek"


# @pytest.mark.skip("TODO")
def test_enqueue_and_dequeue():
    star = Queue()
    star.enqueue("level")
    star.dequeue()
    assert star.is_empty() is True


# @pytest.mark.skip("TODO")
def test_size():
    biggie = Queue()
    listnodes = [1, 2, 3, 4, 5, 6, 7, 8]
    while listnodes:
        biggie.enqueue(listnodes.pop())
    with pytest.raises(Exception):
        biggie.enqueue(9)


# @pytest.mark.skip("TODO")
def test_size_of_queue():
    orange = Queue()
    orange.enqueue("lemon")
    orange.enqueue("candy")
    orange.enqueue("drops")
    assert orange.get_size() == ('Size of queue: 3', 'Max size allowed: 8')


# @pytest.mark.skip("TODO")
def test_enqueue_dequeue_one():
    bq = Queue()
    bq.enqueue("rainbow")
    actual = bq.dequeue()
    expected = "rainbow"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_enqueue_dequeue_two():
    bq = Queue()
    bq.enqueue("pride")
    bq.enqueue("month")
    bq.enqueue("bae")

    actual = bq.dequeue()
    expected = "pride"
    assert actual == expected

    actual = bq.dequeue()
    expected = "month"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_enqueue_dequeue_enqueue_dequeue():
    bq = Queue()
    bq.enqueue("rim")
    bq.enqueue("rim")
    bq.enqueue("tim")

    bq.dequeue()

    bq.enqueue("tagi")
    bq.enqueue("dim")

    actual = [bq.dequeue(), bq.dequeue(), bq.dequeue(), bq.dequeue()]

    expected = ["rim", "tim", "tagi", "dim"]

    assert actual == expected
