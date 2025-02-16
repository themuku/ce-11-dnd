from enum import Enum

from character import ClassesEnum


class Weapon(Enum):
    KATANA = "KATANA"
    BOW = "BOW"
    SPEAR = "SPEAR"
    SWORD = "SWORD"
    AXE = "AXE"
    STAFF = "STAFF"
    DAGGER = "DAGGER"
    NUCLEAR_BOMB = "NUCLEAR_BOMB"
    MACE = "MACE"

class Inventory:
    weapons = []
    potions = []
    artifacts = []
    books = []

    def drop_weapon(self, weapon: Weapon):
        try:
            dropped_item_index = self.weapons.index(weapon)
            return self.weapons.pop(dropped_item_index)
        except ValueError:
            print("Weapon not found in inventory")
            return None

    def add_weapon(self, char_class: ClassesEnum):
        match char_class:
            case ClassesEnum.SAMURAI:
                self.weapons.append(Weapon.KATANA)
            case ClassesEnum.PEON:
                self.weapons.append(Weapon.NUCLEAR_BOMB)
            case ClassesEnum.HOGRIDER:
                self.weapons.append(Weapon.MACE)
            case ClassesEnum.WIZARD:
                self.weapons.append(Weapon.STAFF)
                # TODO