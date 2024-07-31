import pytest
from stack_queue_animal_shelter.stack_queue_animal_shelter import AnimalShelter, Dog, Cat


# @pytest.mark.skip("TODO")
def test_single_cat():
    shelter = AnimalShelter()
    cat = Cat()
    shelter.enqueue_12(cat)
    actual = shelter.dequeue_12("cat")
    expected = cat
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_single_dog():
    shelter = AnimalShelter()
    dog = Dog()
    shelter.enqueue_12(dog)
    actual = shelter.dequeue_12("dog")
    expected = dog
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_dog_preferred_but_cat_in_front():
    shelter = AnimalShelter()
    cat = Cat()
    dog = Dog()
    shelter.enqueue_12(cat)
    shelter.enqueue_12(dog)
    actual = shelter.dequeue_12("dog")
    expected = dog
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_dog_then_cat():
    shelter = AnimalShelter()
    cat = Cat()
    dog = Dog()
    shelter.enqueue_12(dog)
    shelter.enqueue_12(cat)
    shelter.dequeue_12("dog")
    actual = shelter.dequeue_12("cat")
    expected = cat
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_bad_pref():
    shelter = AnimalShelter()
    cat = Cat()
    dog = Dog()
    shelter.enqueue_12(dog)
    shelter.enqueue_12(cat)
    shelter.dequeue_12("dog")
    actual = shelter.dequeue_12("lizard")
    expected = None
    assert expected == actual
