import pytest

from animal import Animal


def test_animal_creation():
    animal = Animal(1, "Max", "Dog", 3)

    assert animal.animal_id == 1
    assert animal.name == "Max"
    assert animal.species == "Dog"
    assert animal.age == 3
    assert animal.status == "Available"


def test_animal_to_dict():
    animal = Animal(1, "Max", "Dog", 3)

    result = animal.to_dict()

    assert result == {
        "animal_id": 1,
        "name": "Max",
        "species": "Dog",
        "age": 3,
        "status": "Available",
    }


def test_animal_rejects_invalid_age():
    with pytest.raises(ValueError):
        Animal(1, "Max", "Dog", -1)


def test_animal_rejects_non_integer_age():
    with pytest.raises(TypeError):
        Animal(1, "Max", "Dog", "3")


def test_animal_adopt():
    animal = Animal(1, "Max", "Dog", 3)

    animal.adopt()

    assert animal.status == "Adopted"


def test_animal_cannot_be_adopted_twice():
    animal = Animal(1, "Max", "Dog", 3)

    animal.adopt()

    with pytest.raises(ValueError):
        animal.adopt()


def test_animal_set_status():
    animal = Animal(1, "Max", "Dog", 3)

    animal.set_status("Adopted")

    assert animal.status == "Adopted"


def test_animal_rejects_invalid_status():
    animal = Animal(1, "Max", "Dog", 3)

    with pytest.raises(ValueError):
        animal.set_status("Zombie")
