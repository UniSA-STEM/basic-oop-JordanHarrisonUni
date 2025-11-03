"""
File: main.py
Description: Test file for the hacker, rig and asset
Author: Jordan Daniel Harrison
ID: harjd011
Username: JordanHarrisonUni
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Hacker import Hacker
from Asset import Asset
from Rig import Rig

# Test basic hacker setup
def test_basic_setup():
    print("\n--- TEST 1: Basic Setup ---")
    hacker1 = Hacker("Neo")
    hacker2 = Hacker("Trinity")

    print(hacker1)
    print(hacker2)

    hacker1.acquire_rig("Sentinel")
    hacker2.acquire_rig("Nebuchadnezzar")

    print(hacker1)
    print(hacker2)
    return hacker1, hacker2

# Test attacking and breaking of rig
def test_attack_and_break(hacker1, hacker2):
    print("\n--- TEST 2: Attack and Break ---")
    # Launch attacks until target rig breaks
    hacker1.launch_attack(hacker2)
    hacker1.launch_attack(hacker2)
    print(hacker2.get_rig())

# Test repair and upgrade functions
def test_repair_and_upgrade(hacker2):
    print("\n--- TEST 3: Repair and Upgrade ---")
    # Give hacker CryptoToken and HardwarePatch manually for testing
    hacker2._Hacker__inventory.append(Asset.create("CryptoToken"))
    hacker2._Hacker__inventory.append(Asset.create("HardwarePatch"))

    # Try to repair
    hacker2.get_rig().repair(hacker2)

    # Upgrade rig
    hacker2.upgrade_rig()
    print(hacker2.get_rig())

# Test encryption and decryption of items
def test_encryption(hacker1):
    print("\n--- TEST 4: Encryption and Decryption ---")
    # Give hacker a SecurityChip and a DataSpike
    hacker1._Hacker__inventory.append(Asset.create("SecurityChip"))
    hacker1._Hacker__inventory.append(Asset.create("DataSpike"))

    hacker1.encrypt_asset("DataSpike")
    print("Inventory after encryption:")
    for asset in hacker1._Hacker__inventory:
        print(asset)

    # Add another chip to decrypt
    hacker1._Hacker__inventory.append(Asset.create("SecurityChip"))
    hacker1.decrypt_asset("DataSpike")
    print("Inventory after decryption:")
    for asset in hacker1._Hacker__inventory:
        print(asset)

def test_edge_cases(hacker1):
    print("\n--- TEST 5: Edge Cases ---")
    # Try upgrading without a rig
    hacker_no_rig = Hacker("Morpheus")
    hacker_no_rig.upgrade_rig()

    # Try encrypting without a Security Chip
    hacker1.encrypt_asset("DataSpike")

    # Force high trace to block attacks
    hacker1._Hacker__trace_level = 5
    hacker1.launch_attack(hacker_no_rig)

def test_additional_behaviours(hacker):
    print("\n--- TEST 6: Additional Behaviours ---")
    rig = hacker.get_rig()

    # Generate a few assets in the rig
    print("\nGenerating assets:")
    for _ in range(3):
        rig.generate_asset()

    # Check rig condition before taking damage
    print(f"Initial rig condition: {rig.condition()}")

    # Manually simulate taking hits
    rig.take_hit()
    rig.take_hit()
    print(f"Rig condition after hits: {rig.condition()}")

    # Try to repair when already pristine (should print message)
    rig.repair(hacker)

    # Give hacker a CryptoToken to repair properly after damage
    hacker._Hacker__inventory.append(Asset.create("CryptoToken"))
    rig.repair(hacker)
    print(f"Rig condition after repair: {rig.condition()}")

    # Give hacker a new asset and test storing/retrieving
    new_asset = Asset.create("DataSpike")
    hacker._Hacker__inventory.append(new_asset)
    print("\nTesting asset storage and retrieval:")
    hacker.store_asset("DataSpike")
    hacker.retrieve_asset("DataSpike")

    # Fill rig storage to hit capacity limit
    print("\nFilling rig storage to test capacity limit:")
    for _ in range(10):
        rig.store_asset(Asset.create("RemovableDrive"))

    # Show final rig and hacker states
    print("\nFinal states:")
    print(rig)
    print(hacker)

if __name__ == "__main__":
    hacker1, hacker2 = test_basic_setup()
    test_attack_and_break(hacker1, hacker2)
    test_repair_and_upgrade(hacker2)
    test_encryption(hacker1)
    test_edge_cases(hacker1)
    test_additional_behaviours(hacker1)