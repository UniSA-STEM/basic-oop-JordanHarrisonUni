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

if __name__ == "__main__":
    hacker1, hacker2 = test_basic_setup()
    test_attack_and_break(hacker1, hacker2)