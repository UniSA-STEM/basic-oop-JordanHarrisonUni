"""
File: Rig.py
Description: Represents a hacker's rig, which acts similarly to a computer
Author: Jordan Daniel Harrison
ID: harjd011
Username: JordanHarrisonUni
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset, ASSETS
import random
class Rig:

    # Initialisation method, takes 1 parameter name and the rest have default values
    def __init__(self, name):
        self.__name = name
        self.__damage = 0
        self.__broken = False
        self.__upgrade_level = 0
        self.__max_storage = 5
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
        # Threshold for breaking starts at 2 and increases per upgrade level
        threshold = 2 + self.__upgrade_level
        # Upgrades reduce effective damage; higher level = more durable
        damage_reduction = 0.25 * self.__upgrade_level  # each level reduces 25% damage impact
        effective_damage = max(0.25, 1 - damage_reduction)
        self.__damage += effective_damage

        if self.__damage >= threshold:
            self.__broken = True
            print(f"{self.__name} is now broken!")

    def repair(self, hacker):
        # Use a CryptoToken to repair the rig if damaged
        if self.__damage == 0:
            print(f"{self.__name} does not need repairs.")
            return

        token = hacker.scan_inventory("CryptoToken")
        if token is None:
            print(f"{hacker.get_name()} does not have a CryptoToken to repair {self.__name}.")
            return

        self.__damage = 0
        self.__broken = False
        print(f"{self.__name} has been repaired to pristine condition.")

    def upgrade(self):
        # Upgrade the level, CryptoToken logic implemented in Hacker.py
        self.__upgrade_level += 1
        self.__max_storage += 2
        print(f"{self.__name} upgraded to level {self.__upgrade_level}.")


    def generate_asset(self):
        # Randomly generate one asset type
        asset_name = random.choice(list(ASSETS.keys()))
        new_asset = Asset.create(asset_name)
        self.__storage.append(new_asset)
        print(f"{self.__name} generated a new asset: {asset_name}.")

    def store_asset(self, asset):
        # Add asset to storage if capacity allows
        if len(self.__storage) >= self.__max_storage:
            print(f"{self.__name}'s storage is full.")
            return
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
        # Return descriptive condition string
        if self.__broken:
            return f"Broken (Level {self.__upgrade_level})"
        elif self.__damage == 0:
            return f"Pristine (Level {self.__upgrade_level})"
        else:
            return f"Damaged (Level {self.__upgrade_level})"
        
    def __str__(self):
        # Build a readable summary of the rig
        stored_assets = ", ".join(asset.get_name() for asset in self.__storage) if self.__storage else "Empty"
        return f"Rig: {self.__name} | Condition: {self.condition()} | Stored Assets: [{stored_assets}]"
