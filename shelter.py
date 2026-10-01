"""Manage animals in the shelter."""

from animal import Animal


class Shelter:
    """Manage animals stored in the shelter."""

    def __init__(self) -> None:
        """Initialize an empty shelter."""
        self.animals: list[Animal] = []
        self.next_id: int = 1

    def add_animal(self, name: str, species: str, age: int) -> Animal:
        """Create and add an animal to the shelter."""
        animal = Animal(self.next_id, name, species, age)
        self.animals.append(animal)
        self.next_id += 1
        return animal

    def find_animal(self, animal_id: int) -> Animal | None:
        """Find an animal by its ID."""
        for animal in self.animals:
            if animal.animal_id == animal_id:
                return animal

        return None

    def delete_animal(self, animal_id: int) -> bool:
        """Delete an animal by ID."""
        animal = self.find_animal(animal_id)

        if animal:
            self.animals.remove(animal)
            return True

        return False
