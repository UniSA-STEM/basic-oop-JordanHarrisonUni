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

    def get_rig(self):
        return self.__rig
    
    def is_exposed(self):
        return self.__trace_level >= 5

    def acquire_rig(self, rig_name):
        if self.__rig is None:
            # Hacker can only have 1 rig
            print(f"{self.__name} already has a rig.")
            return
        
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
        if self.is_exposed():
            print(f"{self.__name} is too exposed to launch an attack")
            return

        # Ensure hacker has a rig
        if not self.get_rig():
            print(f"{self.__name} has no rig to launch an attack with.")
            return

        spike = self.__rig.release_asset("DataSpike")
        # This will use a decrypted DataSpike if it has one, even if the target has no rig
        if spike is None:
            print(f"{self.__name}'s rig does not have a decrypted Data Spike.")
            return
        
        target_rig = target_hacker.get_rig()
        if target_rig is None:
            print(f"{target_hacker.get_name()} does not have a rig to attack.")
            return
        
        # If all checks pass, launch the attack
        # Increase trace level for risky action
        self.increase_trace(1)
        # Print first so broken message comes after
        print(f"{self.__name} hit {target_hacker.get_name()}'s rig '{target_rig.get_name()}'")
        target_rig.take_hit()

    def extract_assets(self, target_hacker_or_rig):
        """
        if target rig is broken, consume one RemovableDrive (preferably from attacker's rig storage,
        otherwise from hacker inventory) and transfer all unencrypted assets from target rig storage
        into attacker's inventory.
        """
        # Get target rig
        if isinstance(target_hacker_or_rig, Rig):
            target_rig = target_hacker_or_rig
        else:
            # assume it's a Hacker object
            target_rig = target_hacker_or_rig.get_rig() if hasattr(target_hacker_or_rig, "get_rig") else None

        if target_rig is None:
            print("Target has no rig to extract from.")
            return

        if not target_rig.is_broken():
            print("Target rig is not broken, cannot extract.")
            return

        # Try to consume a RemovableDrive from attacker's rig storage first
        drive = None
        if self.has_rig() and self.__rig is not None:
            drive = self.__rig.release_asset("RemovableDrive")

        # Try hacker inventory
        if drive is None:
            drive = self.scan_inventory("RemovableDrive")

        if drive is None:
            print(f"{self.__name} has no RemovableDrive to extract assets with.")
            return

        # Transfer unencrypted assets
        unencrypted_assets = target_rig.return_all_unencrypted_assets()
        if not unencrypted_assets:
            print(f"no unencrypted assets found in {target_rig.get_name()}.")
            return

        for asset in unencrypted_assets:
            self.__inventory.append(asset)

        print(f"{self.__name} extracted {len(unencrypted_assets)} asset(s) from {target_rig.get_name()} (consumed a RemovableDrive).")

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