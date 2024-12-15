import numpy as np


class Field:
    def __init__(self, width: int, height: int, tile_set: list) -> None:
        self.width = width
        self.height = height
        self.field = []
        self.tile_set = tile_set

    def create_field(self, tile_set_num_of_ground: int) -> None:
        for i in range(self.width):
            temp_row = []
            for j in range(self.height):
                temp_row.append(self.tile_set[tile_set_num_of_ground])
            self.field.append(temp_row)

    def create_random_squares(self, num_squares: int, tile_for_squares: int) -> None:
        for _ in range(num_squares):
            start_row = np.random.randint(0, self.width - 1)
            start_col = np.random.randint(0, self.height - 1)
            size = np.random.randint(1, min(self.width - start_row, self.height - start_col))
            for i in range(start_row, min(start_row + size, self.width)):
                for j in range(start_col, min(start_col + size, self.height)):
                    self.field[i][j] = self.tile_set[tile_for_squares]

    def create_random_triangles(self, num_triangles: int, tile_for_triangles: int) -> None:
        for _ in range(num_triangles):
            base_length = np.random.randint(2, min(self.width, self.height))
            height = np.random.randint(1, min(self.width, self.height))
            start_row = np.random.randint(0, self.width - height)
            start_col = np.random.randint(0, self.height - base_length)
            for i in range(height):
                for j in range(base_length - i):
                    self.field[start_row + i][start_col + j] = self.tile_set[tile_for_triangles]

    def display(self) -> None:
        for line in self.field:
            print(*line)

    def show_info_about_tiles(self) -> None:
        for i, symbol in enumerate(self.tile_set, 1):
            print(f"{i}: {symbol}")

    def move_tiles(self, cordX1: int, cordY1: int, cordX2: int, cordY2: int, tile1: str, tile2: str) -> None:
        """
        Swaps two tiles on the field.

        :param cordX1: The x-coordinate of the first tile.
        :param cordY1: The y-coordinate of the first tile.
        :param cordX2: The x-coordinate of the second tile.
        :param cordY2: The y-coordinate of the second tile.
        :param tile1: The symbol of the first tile.
        :param tile2: The symbol of the second tile.
        """
        try:
            if cordX1 < 0 or cordX1 >= len(self.field) or cordY1 < 0 or cordY1 >= len(self.field):
                raise ValueError("Coordinate (cordX1, cordY1) is out of bounds")
            if cordX2 < 0 or cordX2 >= len(self.field) or cordY2 < 0 or cordY2 >= len(self.field):
                raise ValueError("Coordinate (cordX2, cordY2) is out of bounds")

            self.field[cordX1][cordY1], self.field[cordX2][cordY2] = tile2, tile1

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def put_tiles(self, cordX: int, cordY: int, tile: str) -> None:
        """
        Places a tile at the specified coordinates on the field.

        :param cordX: The x-coordinate where the tile should be placed.
        :param cordY: The y-coordinate where the tile should be placed.
        :param tile: The symbol of the tile to place.
        """
        try:
            if cordX < 0 or cordX >= len(self.field):
                raise ValueError("Coordinate (cordX) is out of bounds")
            if cordY < 0 or cordY >= len(self.field):
                raise ValueError("Coordinate (cordY) is out of bounds")

            self.field[cordX][cordY] = tile

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

