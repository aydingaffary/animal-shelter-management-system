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