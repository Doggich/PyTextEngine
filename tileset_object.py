from typing import Any, Iterator
from sys import getsizeof


class TileSet:
    def __init__(self) -> None:
        """
        Initializes an empty TileSet object.
        """
        self.tile_list = {}

    def __len__(self) -> int:
        """
        Returns the number of tiles in the TileSet.
        """
        return len(self.tile_list)

    def __getitem__(self, tile_name: str) -> Any:
        """
        Retrieves a tile symbol by its name.

        :param tile_name: The name of the tile to retrieve.
        :return: The symbol associated with the tile.
        """
        return self.tile_list[tile_name]

    def __delitem__(self, tile_name: str) -> None:
        """
        Deletes a tile from the TileSet by its name.

        :param tile_name: The name of the tile to delete.
        """
        del self.tile_list[tile_name]

    def __iter__(self) -> Iterator:
        """
        Returns an iterator over the tile names in the TileSet.
        """
        return iter(self.tile_list)

    def __sizeof__(self) -> int:
        """
        Returns the size of the tile list in bytes.
        """
        return getsizeof(self.tile_list)

    def append(self, tile_name: str, tile_symbol: str) -> None:
        """
        Adds a new tile to the TileSet.

        :param tile_name: The name of the tile to add.
        :param tile_symbol: The symbol of the tile to add.
        """
        self.tile_list[tile_name] = tile_symbol

    def remove(self, tile_name: str) -> None:
        """
        Removes a tile from the TileSet by its name.

        :param tile_name: The name of the tile to remove.
        """
        self.tile_list.pop(tile_name)

    def get_tile(self, tile_name: str) -> str:
        """
        Retrieves a tile symbol by its name.

        :param tile_name: The name of the tile to retrieve.
        :return: The symbol associated with the tile.
        """
        return self.tile_list[tile_name]

    def display(self) -> None:
        """
        Prints all tiles in the TileSet.
        """
        for name, symbol in self.tile_list.items():
            print(name, symbol)

    def get_tiles(self, list_name: list[str]) -> list[str]:
        """
        Retrieves a list of tile symbols for the specified tile names.

        :param list_name: A list of tile names to retrieve.
        :return: A list of tile symbols.
        """
        return_list = []
        for name in self.tile_list.keys():
            if name in list_name:
                return_list.append(self.tile_list[name])
        return return_list

    def get_all_tiles(self) -> list[str]:
        """
        Retrieves a list of all tile symbols in the TileSet.

        :return: A list of all tile symbols.
        """
        return_list = []
        for name in self.tile_list.keys():
            return_list.append(self.tile_list[name])
        return return_list

    def return_set(self) -> dict[str: str]:
        """
        Returns the entire tile list as a dictionary.

        :return: The dictionary containing all tiles.
        """
        return self.tile_list

    def size_of_tile(self, tile_name: str) -> int:
        """
        Returns the size of a specific tile symbol in bytes.

        :param tile_name: The name of the tile to get the size for.
        :return: The size of the tile symbol in bytes.
        """
        return getsizeof(self.tile_list[tile_name])