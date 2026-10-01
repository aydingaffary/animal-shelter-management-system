"""Handle loading and saving animal data."""

import json
from pathlib import Path

from animal import Animal
from shelter import Shelter


def load_animals(shelter: Shelter, file_path: str | Path) -> None:
    """Load animals from the JSON file."""
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        animal = Animal(
            item["animal_id"],
            item["name"],
            item["species"],
            item["age"],
        )

        animal.set_status(item["status"])
        shelter.animals.append(animal)

    if shelter.animals:
        shelter.next_id = max(animal.animal_id for animal in shelter.animals) + 1


def save_animals(shelter: Shelter, file_path: str | Path) -> None:
    """Save animals to the JSON file."""
    data = []

    for animal in shelter.animals:
        data.append(animal.to_dict())

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
