from character import ClassesEnum, RaceEnum
from player import Player

username = input("Enter username: ")
player = Player(username, race=RaceEnum.HUMAN, char_class=ClassesEnum.SAMURAI)

while True:
    pass