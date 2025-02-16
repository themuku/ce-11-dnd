class Level:
    level = 0
    experience = 0
    experience_to_next = 100

    def level_up(self):
        self.level += self.experience % 100

    def add_experience(self, xp):
        self.experience += xp

        if self.experience >= 100:
            self.level_up()
            self.experience -= 100

        self.experience_to_next = 100 - self.experience