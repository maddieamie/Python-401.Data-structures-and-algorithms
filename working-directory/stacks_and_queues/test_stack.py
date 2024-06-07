import pytest
from stacks_and_queues.stack import Stack


# @pytest.mark.skip("TODO")
def test_get_size():
    biggie = Stack()
    listnodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    while listnodes:
        biggie.push(listnodes.pop())
    with pytest.raises(Exception):
        biggie.push(16)


# @pytest.mark.skip("TODO")
def test_size_of_stack():
    orange = Stack()
    orange.push("lemon")
    orange.push("candy")
    orange.push("drops")
    assert orange.get_size() == ('Size of stack: 3', 'Max size allowed: 15')


# @pytest.mark.skip("TODO")
def test_peek_empty():
    emptyone = Stack()
    with pytest.raises(Exception):
        emptyone.peek()


# @pytest.mark.skip("TODO")
def test_peek_return():
    pab = Stack()
    pab.push("peek")
    pab.push("a")
    pab.push("boo")
    assert pab.peek() == "boo"


# @pytest.mark.skip("TODO")
def test_pop_empty():
    emptyone2 = Stack()
    with pytest.raises(Exception):
        emptyone2.pop()


# @pytest.mark.skip("TODO")
def test_pop_return():
    pops = Stack()
    pops.push("poppin")
    assert pops.pop() == "poppin"


# @pytest.mark.skip("TODO")
def test_pop_and_push():
    star = Stack()
    star.push("level")
    star.pop()
    assert star.is_empty() is True


# @pytest.mark.skip("TODO")
def test_pop_multiple():
    blink = Stack()
    blink.push(23)
    blink.push('you are')
    blink.push('when')
    blink.push('likes you')
    blink.push('nobody')
    blink.pop()
    blink.pop()
    blink.pop()
    blink.pop()
    blink.pop()
    assert blink.is_empty() is True


# @pytest.mark.skip("TODO")
def test_push_multiple():
    ns = Stack()
    ns.push(23)
    ns.push('you are')
    ns.push('when')
    ns.push('likes you')
    ns.push('nobody')
    assert str(ns) == "nobody -> likes you -> when -> you are -> 23 -> Null"


def test_pop_on_empty_stack():
    p = Stack()
    with pytest.raises(Exception):
        p.pop()


def test_peek_on_empty_stack():
    n = Stack()
    with pytest.raises(Exception):
        n.peek()


def test_stack_exists():
    stack = Stack()
    assert stack


def test_stack_is_empty():
    ss = Stack()
    assert ss.is_empty() is True


def test_stack_is_empty_false():
    s = Stack()
    s.push('brrrrr')
    assert s.is_empty() is False

