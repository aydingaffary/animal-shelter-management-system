import json
from main import (
    add_animal,
    get_non_empty_input,
    get_valid_age,
    get_valid_animal_id,
    get_valid_status,
)
from main import add_animal
from shelter import Shelter
from main import (
    add_animal,
    adopt_animal,
    get_non_empty_input,
    get_valid_age,
    get_valid_animal_id,
    get_valid_status,
)
from main import (
    add_animal,
    adopt_animal,
    get_non_empty_input,
    get_valid_age,
    get_valid_animal_id,
    get_valid_status,
)
from main import (
    add_animal,
    adopt_animal,
    get_non_empty_input,
    get_valid_age,
    get_valid_animal_id,
    get_valid_status,
)

def test_get_valid_age(monkeypatch):
    inputs = iter(["5"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = get_valid_age()

    assert result == 5


def test_get_valid_age_retries_after_invalid_input(monkeypatch):
    inputs = iter(["abc", "5"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = get_valid_age()

    assert result == 5


def test_get_valid_age_retries_after_out_of_range_input(monkeypatch):
    inputs = iter(["50", "5"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = get_valid_age()

    assert result == 5


def test_get_non_empty_input(monkeypatch):
    inputs = iter(["Max"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = get_non_empty_input("Animal name: ")

    assert result == "Max"


def test_get_non_empty_input_retries_after_empty_input(monkeypatch):
    inputs = iter(["", "Max"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = get_non_empty_input("Animal name: ")

    assert result == "Max"


def test_get_non_empty_input_retries_after_whitespace(monkeypatch):
    inputs = iter(["   ", "Max"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = get_non_empty_input("Animal name: ")

    assert result == "Max"


def test_get_valid_animal_id(monkeypatch):
    inputs = iter(["12"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = get_valid_animal_id()

    assert result == 12

def test_get_valid_animal_id_retries_after_invalid_input(monkeypatch):
    inputs = iter(["abc", "12"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = get_valid_animal_id()

    assert result == 12

def test_get_valid_status(monkeypatch):
    inputs = iter(["available"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = get_valid_status()

    assert result == "Available"
def test_get_valid_status_retries_after_invalid_input(monkeypatch):
    inputs = iter(["Pending", "Adopted"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = get_valid_status()

    assert result == "Adopted"
def test_add_animal(monkeypatch, tmp_path):
    inputs = iter(["Max", "Dog", "3"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    monkeypatch.setattr("main.DATA_FILE", tmp_path / "animals.json")

    shelter = Shelter()

    add_animal(shelter)

    animal = shelter.find_animal(1)

    assert animal is not None
    assert animal.name == "Max"
    assert animal.species == "Dog"
    assert animal.age == 3
def test_add_animal_saves_to_file(monkeypatch, tmp_path):
    inputs = iter(["Lucy", "Cat", "2"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    file_path = tmp_path / "animals.json"
    monkeypatch.setattr("main.DATA_FILE", file_path)

    shelter = Shelter()

    add_animal(shelter)

    assert file_path.exists()

    data = json.loads(file_path.read_text(encoding="utf-8"))

    assert data == [
        {
            "animal_id": 1,
            "name": "Lucy",
            "species": "Cat",
            "age": 2,
            "status": "Available",
        }
    ]
def test_adopt_animal(monkeypatch, tmp_path):
    shelter = Shelter()
    animal = shelter.add_animal("Max", "Dog", 3)

    monkeypatch.setattr("builtins.input", lambda _: str(animal.animal_id))
    monkeypatch.setattr("main.DATA_FILE", tmp_path / "animals.json")

    adopt_animal(shelter)

    assert animal.status == "Adopted"

def test_adopt_already_adopted_animal(monkeypatch, tmp_path, capsys):
    shelter = Shelter()
    animal = shelter.add_animal("Max", "Dog", 3)
    animal.adopt()

    monkeypatch.setattr(
        "builtins.input",
        lambda _: str(animal.animal_id),
    )
    monkeypatch.setattr(
        "main.DATA_FILE",
        tmp_path / "animals.json",
    )

    adopt_animal(shelter)

    captured = capsys.readouterr()

    assert animal.status == "Adopted"
    assert "already adopted" in captured.out
def test_update_animal(monkeypatch, tmp_path):
    inputs = iter(["1", "Charlie", "Cat", "5"])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs),
    )
    monkeypatch.setattr(
        "main.DATA_FILE",
        tmp_path / "animals.json",
    )

    shelter = Shelter()
    shelter.add_animal("Max", "Dog", 3)

    from main import update_animal

    update_animal(shelter)

    animal = shelter.find_animal(1)

    assert animal is not None
    assert animal.name == "Charlie"
    assert animal.species == "Cat"
    assert animal.age == 5
def test_update_animal_not_found(monkeypatch, capsys):
    inputs = iter(["999"])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs),
    )

    shelter = Shelter()

    from main import update_animal

    update_animal(shelter)

    captured = capsys.readouterr()

    assert "Animal not found." in captured.out
def test_update_animal_saves_to_file(monkeypatch, tmp_path):
    inputs = iter(["1", "Charlie", "Cat", "5"])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs),
    )

    file_path = tmp_path / "animals.json"
    monkeypatch.setattr("main.DATA_FILE", file_path)

    shelter = Shelter()
    shelter.add_animal("Max", "Dog", 3)

    from main import update_animal

    update_animal(shelter)

    data = json.loads(file_path.read_text(encoding="utf-8"))

    assert data == [
        {
            "animal_id": 1,
            "name": "Charlie",
            "species": "Cat",
            "age": 5,
            "status": "Available",
        }
    ]
def test_delete_animal(monkeypatch, tmp_path):
    inputs = iter(["1"])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs),
    )
    monkeypatch.setattr(
        "main.DATA_FILE",
        tmp_path / "animals.json",
    )

    shelter = Shelter()
    shelter.add_animal("Max", "Dog", 3)

    from main import delete_animal

    delete_animal(shelter)

    assert shelter.find_animal(1) is None
def test_delete_animal_not_found(monkeypatch, capsys):
    inputs = iter(["999"])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs),
    )

    shelter = Shelter()

    from main import delete_animal

    delete_animal(shelter)

    captured = capsys.readouterr()

    assert "Animal not found." in captured.out