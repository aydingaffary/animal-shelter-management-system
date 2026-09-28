from animal import Animal


class Shelter:
    """Manage animals in the shelter."""

    def __init__(self) -> None:
        """Initialize an empty shelter."""
        self.animals: list[Animal] = []
        self.next_id: int = 1

    def add_animal(self, animal: Animal) -> None:
        """Add an animal to the shelter."""
        self.animals.append(animal)
        self.next_id += 1

    def find_animal(self, animal_id: int) -> Animal | None:
        """Find an animal by its ID."""
        for animal in self.animals:
            if animal.animal_id == animal_id:
                return animal

        return None

    def delete_animal(self, animal_id: int) -> bool:
        """Delete an animal by its ID."""
        animal = self.find_animal(animal_id)

        if animal:
            self.animals.remove(animal)
            return True

        return False
