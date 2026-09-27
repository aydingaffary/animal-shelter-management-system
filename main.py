

import json
from animal import Animal
from shelter import Shelter


  
def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print('This field cannot be empty.')
def add_animal(shelter):
    name = get_non_empty_input('Animal name: ')
    species = get_non_empty_input('Species: ')

    age = get_valid_age()

    animal = Animal(shelter.next_id, name, species, age)

    return animal
def get_valid_age():
    while True:
        age = input('Age: ')

        if age.isdigit():
            age = int(age)

            if 0 <= age <= 30:
                return age

            print('Age must be between 0 and 30.')
        else:
            print('Age must be a number.')
def get_valid_status():
    while True:
        status = input('Status (Available/Adopted): ').strip().capitalize()

        if status in ['Available', 'Adopted']:
            return status

        print('Invalid status. Please enter Available or Adopted.')
            
def get_valid_animal_id():
    while True:
        animal_id = input('Animal ID: ')

        if animal_id.isdigit():
            return int(animal_id)

        print('Animal ID must be a number.')

def find_animal(shelter):
    animal_id = get_valid_animal_id()

    for animal in shelter.animals:
        if animal.animal_id == animal_id:
            animal.display_info()
            break
    else:
        print('Animal not found.')
def update_animal(shelter):
    animal_id = get_valid_animal_id()

    for animal in shelter.animals:
        if animal.animal_id == animal_id:
            new_name = get_non_empty_input('New name: ')
            animal.name = new_name

            new_species = get_non_empty_input('New species: ')
            animal.species = new_species

            new_age = get_valid_age()
            animal.age = new_age

            animal.display_info()
            break
    else:
        print('Animal not found.')
def delete_animal(shelter):
    animal_id = get_valid_animal_id()

    for animal in shelter.animals:
        if animal.animal_id == animal_id:
            shelter.animals.remove(animal)
            print('Animal deleted successfully.')
            break
    else:
        print('Animal not found.')

def adopt_animal(shelter):
    animal_id = get_valid_animal_id()

    for animal in shelter.animals:
        if animal.animal_id == animal_id:
            if animal.status == 'Adopted':
                print('Animal is already adopted.')
            else:
                animal.status = 'Adopted'
                print('Animal adopted successfully.')

            break
    else:
        print('Animal not found.')
def show_animals_by_status(shelter):
    status = get_valid_status()
    found = False

    for animal in shelter.animals:
        if animal.status == status:
            animal.display_info()
            found = True

    if not found:
        print('No animals found.')
with open('data/animals.json', 'r') as file:
    data = json.load(file)

print(data)        
shelter = Shelter()

while True:
    print('1. Add animal')
    print('2. Find animal')
    print('3. Update animal')
    print('4. Delete animal')
    print('5. Adopt animal')
    print('6. Show animals by status')
    print('7. Exit')
    choice = input('Choose an option: ')
    
    if choice == '1':
       animal = add_animal(shelter)
       shelter.animals.append(animal)
       shelter.next_id += 1
  
   
    elif choice == '2':
        find_animal(shelter)

    elif choice == '3':
        update_animal(shelter)

    elif choice == '4':
        delete_animal(shelter)

    elif choice == '5':
        adopt_animal(shelter)

    elif choice == '6':
        show_animals_by_status(shelter)

    elif choice == '7':
        break

    else:
        print('Invalid option. Please try again.')


