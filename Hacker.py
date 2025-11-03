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
    
    def is_exposed(self):
        return self.__trace_level >= 5

    def acquire_rig(self, rig_name):
        token = self.scan_inventory("CryptoToken")
        if token is None:
            # If there isn't any CryptoToken's found in the user's inventory, error out
            print(f"{self.__name} does not have enough CryptoTokens to acquire a rig.")
            return
        
        # Create a new rig instance and assign it to the user
        self.__rig = Rig(rig_name)
        print(f"{self.__name} has activated rig '{rig_name}'!")

    def increase_trace(self, amount=1):
        # Increases the trace level by either a specific amount or 1 if not provided.
        self.__trace_level += amount
        return

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
        for asset in self.__inventory:
            # Loop through the entire inventory until you find the first occurance of a match
            if asset.get_name() == asset_name:
                # Remove the item from the inventory and return the result
                self.__inventory.remove(asset)
                return asset
        # If there wasn't one found, it will reach this part of the code, and return None
        return None

    def __str__(self):
        # Return a formatted string showing hacker details and inventory contents
        pass