from animal import Animal
from data_manager import load_animals, save_animals
from shelter import Shelter


def get_non_empty_input(prompt: str) -> str:
    """Get a non-empty string from the user."""
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("This field cannot be empty.")


def get_valid_age() -> int:
    """Get a valid animal age from the user."""
    while True:
        age = input("Age: ")

        if age.isdigit():
            age = int(age)

            if 0 <= age <= 30:
                return age

            print("Age must be between 0 and 30.")
        else:
            print("Age must be a number.")


def get_valid_status() -> str:
    """Get a valid animal status from the user."""
    while True:
        status = input("Status (Available/Adopted): ").strip().capitalize()

        if status in ["Available", "Adopted"]:
            return status

        print("Invalid status. Please enter Available or Adopted.")


def get_valid_animal_id() -> int:
    """Get a valid animal ID from the user."""
    while True:
        animal_id = input("Animal ID: ")

        if animal_id.isdigit():
            return int(animal_id)

        print("Animal ID must be a number.")


def add_animal(shelter: Shelter) -> None:
    """Add a new animal to the shelter."""
    name = get_non_empty_input("Animal name: ")
    species = get_non_empty_input("Species: ")
    age = get_valid_age()

    animal = Animal(shelter.next_id, name, species, age)

    shelter.add_animal(animal)
    save_animals(shelter)

    print("Animal added successfully.")


def find_animal(shelter: Shelter) -> None:
    """Find and display an animal by ID."""
    animal_id = get_valid_animal_id()
    animal = shelter.find_animal(animal_id)

    if animal:
        animal.display_info()
    else:
        print("Animal not found.")


def update_animal(shelter: Shelter) -> None:
    """Update an existing animal."""
    animal_id = get_valid_animal_id()
    animal = shelter.find_animal(animal_id)

    if animal:
        new_name = get_non_empty_input("New name: ")
        animal.name = new_name

        new_species = get_non_empty_input("New species: ")
        animal.species = new_species

        new_age = get_valid_age()
        animal.age = new_age

        save_animals(shelter)

        print("Animal updated successfully.")
        animal.display_info()
    else:
        print("Animal not found.")


def delete_animal(shelter: Shelter) -> None:
    """Delete an animal by ID."""
    animal_id = get_valid_animal_id()

    if shelter.delete_animal(animal_id):
        save_animals(shelter)
        print("Animal deleted successfully.")
    else:
        print("Animal not found.")


def adopt_animal(shelter: Shelter) -> None:
    """Adopt an animal by ID."""
    animal_id = get_valid_animal_id()
    animal = shelter.find_animal(animal_id)

    if animal:
        if animal.status == "Adopted":
            print("Animal is already adopted.")
        else:
            animal.status = "Adopted"
            save_animals(shelter)
            print("Animal adopted successfully.")
    else:
        print("Animal not found.")


def show_animals_by_status(shelter: Shelter) -> None:
    """Display animals with a specific status."""
    status = get_valid_status()
    found = False

    for animal in shelter.animals:
        if animal.status == status:
            animal.display_info()
            found = True

    if not found:
        print("No animals found.")


def main() -> None:
    """Run the animal shelter application."""
    shelter = Shelter()
    load_animals(shelter)

    while True:
        print("\n1. Add animal")
        print("2. Find animal")
        print("3. Update animal")
        print("4. Delete animal")
        print("5. Adopt animal")
        print("6. Show animals by status")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_animal(shelter)

        elif choice == "2":
            find_animal(shelter)

        elif choice == "3":
            update_animal(shelter)

        elif choice == "4":
            delete_animal(shelter)

        elif choice == "5":
            adopt_animal(shelter)

        elif choice == "6":
            show_animals_by_status(shelter)

        elif choice == "7":
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
