from inventory import Inventory, Weapon
from enum import Enum
from level import Level


class RaceEnum(Enum):
    HUMAN = "HUMAN"
    ORC = "ORC"
    ELF = "ELF"

class ClassesEnum(Enum):
    SAMURAI = "SAMURAI"
    WIZARD = "WIZARD"
    KNIGHT = "KNIGHT"
    ARCHER = "ARCHER"
    HORSEMAN = "HORSEMAN"
    ALCHEMIST = "ALCHEMIST"
    PEON = "PEON"
    HOGRIDER = "HOGRIDER"
    SPEAR = "SPEAR"
    ASSASSIN = "ASSASSIN"


class Character:
    name: str
    health: float
    char_class: ClassesEnum
    stamina: float
    manna: float or None
    race: RaceEnum
    inventory: Inventory
    level: Level

    def __init__(self, name, char_class: ClassesEnum, race: RaceEnum):
        self.name = name

        match race:
            case RaceEnum.HUMAN:
                if char_class in [ClassesEnum.SAMURAI, ClassesEnum.ARCHER, ClassesEnum.ALCHEMIST, ClassesEnum.HORSEMAN, ClassesEnum.KNIGHT, ClassesEnum.WIZARD]:
                    self.char_class = char_class
                else:
                    print("Human race doesn't include this class use these instead (" + str(c for c in ClassesEnum) + ")")
#                    ...

                match self.char_class:
                    case ClassesEnum.SAMURAI:
                        self.health = 100
                        self.stamina = 110
                    case ClassesEnum.KNIGHT:
                        self.health = 120
                        self.stamina = 80
                    case ClassesEnum.WIZARD:
                        self.manna = 170
                        self.health = 80
                        self.stamina = 70
                    case ClassesEnum.ALCHEMIST:
                        self.manna = 60
                        self.stamina = 80
                        self.health = 90
                    case ClassesEnum.HORSEMAN:
                        self.stamina = 160
                        self.health = 80
                    case ClassesEnum.ARCHER:
                        self.stamina = 120
                        self.health = 80

            case RaceEnum.ELF:
                self.health = 80
                self.stamina = 70

                if char_class in [ClassesEnum.ARCHER, ClassesEnum.WIZARD, ClassesEnum.ASSASSIN, ClassesEnum.ALCHEMIST]:
                    self.char_class = char_class
                else:
                    print("Elf race doesn't include this class use these instead (" + str(c for c in [
                        ClassesEnum.ARCHER, ClassesEnum.WIZARD, ClassesEnum.ASSASSIN, ClassesEnum.ALCHEMIST]) + ")")
                #                    ...

                match self.char_class:
                    case ClassesEnum.WIZARD:
                        self.manna = 200
                        self.health = 70
                        self.stamina = 50
                    case ClassesEnum.ALCHEMIST:
                        self.manna = 50
                        self.health = 70
                        self.stamina = 70
                    case ClassesEnum.ARCHER:
                        self.health = 70
                        self.stamina = 100
                    case ClassesEnum.ASSASSIN:
                        self.stamina = 200
                        self.health = 80

            case RaceEnum.ORC:
                self.health = 80
                self.stamina = 70

                if char_class in [ClassesEnum.SPEAR, ClassesEnum.PEON, ClassesEnum.HOGRIDER]:
                    self.char_class = char_class
                else:
                    print("Elf race doesn't include this class use these instead (" + str(c for c in [
                        ClassesEnum.SPEAR, ClassesEnum.PEON, ClassesEnum.HOGRIDER]) + ")")

                match self.char_class:
                    case ClassesEnum.HOGRIDER:
                        self.stamina = 200
                        self.health = 140
                    case ClassesEnum.SPEAR:
                        self.stamina = 100
                        self.health = 80
                    case ClassesEnum.PEON:
                        self.stamina = 110
                        self.health = 100
