
class Player:
    def __init__(self, health: int, inventory_size: int, age: int, exp_level: int, exp_points: int, stats: dict) -> None:
        self.health = health
        self.inventory_size = inventory_size
        self.age = age
        self.exp_level = exp_level
        self.exp_points = exp_points
        self.stats = stats

    def __str__(self) -> str:
        return f"hp: {self.health}" \
               f"\ninventory size: {self.inventory_size}" \
               f"\nage: {self.age}" \
               f"\nexp level: {self.exp_level}" \
               f"\nexp points: {self.exp_points}" \
               f"\nstats: {self.stats}"

    def get_params(self) -> list:
        return [self.health, self.inventory_size, self.age, self.exp_level, self.stats]
