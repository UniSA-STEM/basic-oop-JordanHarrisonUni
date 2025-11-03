"""
File: Rig.py
Description: Represents a hacker's rig, which acts similarly to a computer
Author: Jordan Daniel Harrison
ID: harjd011
Username: JordanHarrisonUni
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Rig:

    # Initialisation method, takes 1 parameter name and the rest have default values
    def __init__(self, name):
        self.__name = name
        self.__damage = 0
        self.__broken = False
        self.__upgrade_level = 0
        # Assignment states each rig starts with 2 data spikes and 1 removable drive
        # Code for Asset init is not made yet so this may need to be changed in the future
        self.__storage = [
            Asset("Data Spike", "Used to attack other rigs."),
            Asset("Data Spike", "Used to attack other rigs."),
            Asset("Removable Drive", "Used to extract assets from broken rigs.")
        ]

    # Getters
    def get_name(self):
        return self.__name

    def is_broken(self):
        return self.__broken
    
    # Placeholder methods, will add implementation later
    def take_hit(self):
        # Increase rig damage
        pass

    def repair(self):
        # Repair rig if damaged
        pass

    def upgrade(self):
        # Upgrade the rig
        pass

    def generate_asset(self):
        # Generate a new random asset
        pass

    def store_asset(self, asset):
        # Add an asset to storage
        pass

    def release_asset(self, asset_name):
        # Remove and return an asset by name
        pass

    def condition(self):
        # Return the rig’s condition string
        pass