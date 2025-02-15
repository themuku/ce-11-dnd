CHARS = [
    {
        "race": "HUMAN",
        "classes": ["SAMURAI", "WIZARD", "KNIGHT", "ARCHER", "HORSEMAN", "ALCHEMIST"]
    },
    {
        "race": "ORC",
        "classes": ["ARCHER", "PEON", "HOGRIDER", "SPEAR"]
    },
    {
        "race": "ELF",
        "classes": ["WIZARD", "ARCHER", "ALCHEMIST"]
    },
]

class Character:
    name: str
    health: float
    char_class: str
    stamina: float
    manna: float or None
    race: str
    inventory = []

    def __init__(self, name, char_class, race):
        self.name = name

        # Mapping of race and class
        for c in CHARS:
            if race == c["race"] and char_class in c["classes"]:
                self.race = race
                self.char_class = char_class

        if self.race == CHARS[2]["race"]:
            self.stamina = 60
            self.health = 80
        elif self.race == CHARS[0]["race"]:
            self.health = 100
            if self.char_class == CHARS[0]["classes"][0] or self.char_class == CHARS[0]["classes"][2]:
                self.stamina = 120
            else:
                self.stamina = 90

        if self.race == "ORC":
            self.stamina = 150
            self.health = 110

        if self.race == CHARS[2]["race"] and self.char_class == CHARS[2]["classes"][0]:
            self.manna = 150
        elif self.race == CHARS[0]["race"] and self.char_class == CHARS[0]["classes"][1]:
            self.manna = 100
