import json

from data_manager import load_animals, save_animals
from shelter import Shelter


def test_save_animals(tmp_path):
    shelter = Shelter()

    shelter.add_animal("Max", "Dog", 3)
    shelter.add_animal("Lucy", "Cat", 2)

    file_path = tmp_path / "animals.json"

    save_animals(shelter, file_path)

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    assert len(data) == 2
    assert data[0]["name"] == "Max"
    assert data[1]["name"] == "Lucy"


def test_load_animals(tmp_path):
    shelter = Shelter()

    max_animal = shelter.add_animal("Max", "Dog", 3)
    lucy_animal = shelter.add_animal("Lucy", "Cat", 2)

    lucy_animal.status = "Adopted"

    file_path = tmp_path / "animals.json"

    save_animals(shelter, file_path)

    new_shelter = Shelter()

    load_animals(new_shelter, file_path)

    assert len(new_shelter.animals) == 2

    loaded_max = new_shelter.find_animal(max_animal.animal_id)
    loaded_lucy = new_shelter.find_animal(lucy_animal.animal_id)

    assert loaded_max.name == "Max"
    assert loaded_max.species == "Dog"
    assert loaded_max.age == 3
    assert loaded_max.status == "Available"

    assert loaded_lucy.name == "Lucy"
    assert loaded_lucy.species == "Cat"
    assert loaded_lucy.age == 2
    assert loaded_lucy.status == "Adopted"

    assert new_shelter.next_id == 3
