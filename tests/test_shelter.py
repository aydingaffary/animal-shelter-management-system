from shelter import Shelter


def test_add_animal():
    shelter = Shelter()

    animal = shelter.add_animal("Max", "Dog", 3)

    assert animal in shelter.animals
    assert len(shelter.animals) == 1


def test_add_animal_assigns_id():
    shelter = Shelter()

    animal = shelter.add_animal("Max", "Dog", 3)

    assert animal.animal_id == 1
    assert animal.name == "Max"
    assert animal.species == "Dog"
    assert animal.age == 3


def test_find_animal():
    shelter = Shelter()

    animal = shelter.add_animal("Max", "Dog", 3)

    result = shelter.find_animal(animal.animal_id)

    assert result == animal


def test_find_animal_not_found():
    shelter = Shelter()

    result = shelter.find_animal(99)

    assert result is None


def test_delete_animal():
    shelter = Shelter()

    animal = shelter.add_animal("Max", "Dog", 3)

    result = shelter.delete_animal(animal.animal_id)

    assert result is True
    assert animal not in shelter.animals
    assert len(shelter.animals) == 0


def test_delete_animal_not_found():
    shelter = Shelter()

    result = shelter.delete_animal(99)

    assert result is False


def test_id_increases_after_delete():
    shelter = Shelter()

    first_animal = shelter.add_animal("Max", "Dog", 3)
    shelter.delete_animal(first_animal.animal_id)

    new_animal = shelter.add_animal("Charlie", "Rabbit", 1)

    assert new_animal.animal_id == 2


def test_multiple_animals_get_unique_ids():
    shelter = Shelter()

    animal1 = shelter.add_animal("Max", "Dog", 3)
    animal2 = shelter.add_animal("Lucy", "Cat", 2)
    animal3 = shelter.add_animal("Charlie", "Rabbit", 1)

    assert animal1.animal_id == 1
    assert animal2.animal_id == 2
    assert animal3.animal_id == 3


def test_add_animal_after_delete_keeps_next_id():
    shelter = Shelter()

    first_animal = shelter.add_animal("Max", "Dog", 3)
    shelter.add_animal("Lucy", "Cat", 2)

    shelter.delete_animal(first_animal.animal_id)

    new_animal = shelter.add_animal("Rocky", "Dog", 4)

    assert new_animal.animal_id == 3
