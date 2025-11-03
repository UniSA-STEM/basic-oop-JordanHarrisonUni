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
    "RemovableDrive": "Used to extract assets from broken rigs."
}

class Asset:

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

    # Placeholder methods, will add implementation later
    def encrypt(self):
        # Mark asset as encrypted
        pass

    def decrypt(self):
        # Mark asset as decrypted
        pass

    def __str__(self):
        # Return a string showing name, description and encryption status
        pass