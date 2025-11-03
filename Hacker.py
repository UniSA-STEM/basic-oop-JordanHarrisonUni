"""
File: Hacker.py
Description: Represents a hacker who can interact with rigs and assets
Author: Jordan Daniel Harrison
ID: harjd011
Username: JordanHarrisonUni
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset
from Rig import Rig

class Hacker:
    # Initialisation method, takes 1 parameter name and sets defaults
    def __init__(self, name):
        self.__name = name
        self.__inventory = [Asset.create("CryptoToken")]
        self.__rig = None
        self.__trace_level = 0

    # Getters
    def get_name(self):
        return self.__name

    def get_trace_level(self):
        return self.__trace_level

    def has_rig(self):
        return self.__rig

    # Placeholder methods, will add implementation later
    def acquire_rig(self):
        # Acquire a new rig
        pass

    def launch_attack(self, target_hacker):
        # Use a Data Spike to damage another hacker's rig
        pass

    def extract_assets(self, target_rig):
        # Extract unencrypted assets from a broken rig
        pass

    def encrypt_asset(self, asset_name):
        # Encrypt an asset in inventory or rig storage
        pass

    def decrypt_asset(self, asset_name):
        # Decrypt an asset in inventory or rig storage
        pass

    def upgrade_rig(self):
        # Use a Hardware Patch to upgrade the rig
        pass

    def store_asset(self, asset_name):
        # Move an asset from inventory to rig storage
        pass

    def retrieve_asset(self, asset_name):
        # Move an asset from rig storage to inventory
        pass

    def scan_inventory(self, asset_name):
        # Search for and remove an asset by name
        pass

    def __str__(self):
        # Return a formatted string showing hacker details and inventory contents
        pass