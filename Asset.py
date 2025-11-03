"""
File: Asset.py
Description: A digital asset that can be stored and used by hackers/rigs
Author: Jordan Daniel Harrison
ID: harjd011
Username: JordanHarrisonUni
This is my own work as defined by the University's Academic Misconduct Policy.
"""
ASSETS = {
    "CryptoToken": "Used to purchase and repair rigs.",
    "DataSpike": "Used to attack other rigs.",
    "RemovableDrive": "Used to extract assets from broken rigs.",
    "SecurityChip": "Used to encrypt or decrypt an asset."
}

class Asset:

    # @classmethod allows us to called on Asset rather than an instance of.
    @classmethod
    def create(cls, asset_name):
        # Creates an asset by using one from our defined list
        if asset_name not in ASSETS:
            raise ValueError(f"Unknown asset: {asset_name}")
        return cls(asset_name, ASSETS[asset_name])

    # Initialisation method, takes parameters for name and description
    def __init__(self, name, description):
        self.__name = name
        self.__description = description
        self.__encrypted = False

    # Getters
    def get_name(self):
        return self.__name

    def is_encrypted(self):
        return self.__encrypted

    def encrypt(self, hacker):
        # Only encrypt if it's not already encrypted and a Security Chip is available
        if self.__encrypted:
            print(f"{self.__name} is already encrypted.")
            return

        chip = hacker.scan_inventory("SecurityChip")
        if chip is None:
            print(f"{hacker.get_name()} does not have a Security Chip to encrypt {self.__name}.")
            return

        self.__encrypted = True
        print(f"{self.__name} has been encrypted using a Security Chip.")

    def decrypt(self, hacker):
        # Only decrypt if currently encrypted and a Security Chip is available
        if not self.__encrypted:
            print(f"{self.__name} is already unencrypted.")
            return

        chip = hacker.scan_inventory("SecurityChip")
        if chip is None:
            print(f"{hacker.get_name()} does not have a Security Chip to decrypt {self.__name}.")
            return

        self.__encrypted = False
        print(f"{self.__name} has been decrypted using a Security Chip.")

    def __str__(self):
        # Return a string showing name, description and encryption status
        pass