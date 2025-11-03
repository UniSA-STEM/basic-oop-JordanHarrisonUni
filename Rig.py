"""
File: Rig.py
Description: Represents a hacker's rig, which acts similarly to a computer
Author: Jordan Daniel Harrison
ID: harjd011
Username: JordanHarrisonUni
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset
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
            Asset.create("DataSpike"),
            Asset.create("DataSpike"),
            Asset.create("RemovableDrive")
        ]

    # Getters
    def get_name(self):
        return self.__name

    def is_broken(self):
        return self.__broken
    
    def take_hit(self):
        # Threshold for maximum damage, starts at 2 and increases per level
        threshold = 2 + self.__upgrade_level
        self.__damage += 1
        if self.__damage >= threshold:
            self.__broken = True
            print(f"{self.__name} is now broken!")

    def repair(self):
        if self.__damage == 0:
            print(f"{self.__name} does not need repairs.")
            return
        self.__damage = 0
        self.__broken = False
        print(f"{self.__name} has been repaired to pristine condition.")

    def upgrade(self):
        # Upgrade the level, CryptoToken logic implemented in Hacker.py
        self.__upgrade_level += 1
        print(f"{self.__name} upgraded to level {self.__upgrade_level}.")
        return

    def generate_asset(self):
        # Generate a new random asset
        pass

    def store_asset(self, asset):
        # Add asset to storage
        self.__storage.append(asset)

    def release_asset(self, asset_name):
        # Release an asset from the storage
        for asset in list(self.__storage):
            if asset.get_name() == asset_name and not asset.is_encrypted():
                self.__storage.remove(asset)
                return asset
        return None
    
    def return_all_unencrypted_assets(self):
        # Return a list of all unencrypted assets from storage.
        unencrypted = [asset for asset in self.__storage if not asset.is_encrypted()]
        self.__storage = [asset for asset in self.__storage if asset.is_encrypted()]
        return unencrypted

    def condition(self):
        # Return the rig’s condition string
        pass