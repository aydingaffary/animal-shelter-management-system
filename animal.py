# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 16:51:05 2026

@author: aydin
"""

class Animal:
    def __init__(self, animal_id, name, species, age):
        self.animal_id = animal_id
        self.name = name
        self.species = species
        self.age = age
        self.status = 'Available'

    def to_dict(self):
        return {
            'animal_id': self.animal_id,
            'name': self.name,
            'species': self.species,
            'age': self.age,
            'status': self.status
        }

    def display_info(self):
        print(
            f'ID: {self.animal_id} | '
            f'Name: {self.name} | '
            f'Species: {self.species} | '
            f'Age: {self.age} | '
            f'Status: {self.status}'
        )