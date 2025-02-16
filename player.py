from character import Character, RaceEnum, ClassesEnum


class Player(Character):
    def __init__(self, name, char_class: ClassesEnum, race: RaceEnum):
        super().__init__(name, char_class, race)