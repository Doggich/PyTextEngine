from math import sqrt


class CrewMember:
    def __init__(self, name: str, role: str, skill: list):
        self.name = name
        self.role = role
        self.skill = skill

    def __str__(self):
        return f"{self.name} ({self.role}): {self.skill}"

    def choice_skill_param(self, num: int):
        return self.skill[num]


class Ship:
    def __init__(self, name: str, crew: list, dmg: int, shield: int, speed: int, cannons: int, fuel: int,
                 max_fuel: int):
        self.name = name
        self.crew = crew
        self.dmg = dmg * 1.2
        self.shield = shield
        self.speed = int(speed * 0.003003)
        self.cannons = cannons
        self.fuel = fuel
        self.max_fuel = max_fuel

    def __str__(self):
        return f"{self.name} ({self.dmg} dmg, {self.shield} shield, {self.speed} speed, {self.cannons} cannons): {self.crew}"

    def append_crew(self, crew_member: CrewMember):
        self.crew.append(crew_member)

    def remove_crew(self, crew_member: CrewMember):
        self.crew.remove(crew_member)

    def print_crew(self):
        return "".join([str(crew_member) + "\n" for crew_member in self.crew])

    def refuel(self, count: int):
        if self.max_fuel >= self.fuel + count:
            self.fuel += count
            return True
        else:
            return False

    def attack(self):
        return self.dmg * self.cannons

    def time_for_teleport(self, radius1: int, x_cord1: float, y_cord1: float, radius2: int, x_cord2: float,
                          y_cord2: float):
        self.fuel -= sqrt(pow(x_cord2 - x_cord1, 2) + pow(y_cord2 - y_cord1, 2)) * 0.02
        return (sqrt(pow(x_cord2 - x_cord1, 2) + pow(y_cord2 - y_cord1, 2)) - (radius1 + radius2)) / self.speed ** 2
