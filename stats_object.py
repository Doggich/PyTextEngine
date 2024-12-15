class Stats:
    def __init__(self, speed: int, strength: int, intelegence: int, stamina: int) -> None:
        self.speed = speed
        self.strength = strength
        self.intelligence = intelegence
        self.stamina = stamina

    def __str__(self) -> str:
        return f"\n\tspeed: {self.speed} " \
               f"\n\tstrength: {self.strength}" \
               f"\n\tintelligence: {self.intelligence}" \
               f"\n\tstamina: {self.stamina}"

    def get_stats(self) -> dict:
        return {"speed": self.speed, "strength": self.strength, "intelligence": self.intelligence, "stamina": self. stamina}

    def add_level(self, stats_index: int) -> None:
        if stats_index == 1:
            self.speed += 1
        elif stats_index == 2:
            self.strength += 1
        elif stats_index == 3:
            self.intelligence += 1
        elif stats_index == 4:
            self.stamina += 1






