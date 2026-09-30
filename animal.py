# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 16:51:05 2026

@author: aydin
"""


class Animal:
    """Represent an animal in the shelter."""

    VALID_STATUSES = {"Available", "Adopted"}

    def __init__(self, animal_id, name, species, age):
        """Initialize an animal."""
        if not isinstance(age, int):
            raise TypeError("Age must be an integer.")

        if age < 0 or age > 30:
            raise ValueError("Age must be between 0 and 30.")

        self.animal_id = animal_id
        self.name = name
        self.species = species
        self.age = age
        self.status = "Available"

    def to_dict(self):
        """Convert the animal object to a dictionary."""
        return {
            "animal_id": self.animal_id,
            "name": self.name,
            "species": self.species,
            "age": self.age,
            "status": self.status,
        }

    def adopt(self):
        """Adopt the animal."""
        if self.status == "Adopted":
            raise ValueError("Animal is already adopted.")

        self.status = "Adopted"

    def set_status(self, status):
        """Set the animal status."""
        if status not in self.VALID_STATUSES:
            raise ValueError("Invalid animal status.")

        self.status = status

    def display_info(self):
        """Display the animal information."""
        print(
            f"ID: {self.animal_id} | "
            f"Name: {self.name} | "
            f"Species: {self.species} | "
            f"Age: {self.age} | "
            f"Status: {self.status}"
        )
