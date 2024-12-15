from tileset_object import TileSet
from typing import Any, Iterator
from sys import getsizeof


class Atlas:
    def __init__(self) -> None:
        """
        Initializes an empty Atlas object.
        """
        self.atlas_list = {}

    def __len__(self) -> int:
        """
        Returns the number of pages in the Atlas.
        """
        return len(self.atlas_list)

    def __getitem__(self, page_name: str) -> Any:
        """
        Retrieves an object from the Atlas by its page name.

        :param page_name: The name of the page to retrieve.
        :return: The object associated with the page.
        """
        return self.atlas_list[page_name]

    def __delitem__(self, page_name: str) -> None:
        """
        Deletes a page from the Atlas by its name.

        :param page_name: The name of the page to delete.
        """
        del self.atlas_list[page_name]

    def __iter__(self) -> Iterator:
        """
        Returns an iterator over the page names in the Atlas.
        """
        return iter(self.atlas_list)

    def __sizeof__(self) -> int:
        """
        Returns the size of the atlas list in bytes.
        """
        return getsizeof(self.atlas_list)

    def append(self, page_name: str, object_: Any) -> None:
        """
        Adds a new page to the Atlas.

        :param page_name: The name of the page to add.
        :param object_: The object to associate with the page.
        """
        self.atlas_list[page_name] = object_

    def remove(self, page_name: str) -> None:
        """
        Removes a page from the Atlas by its name.

        :param page_name: The name of the page to remove.
        """
        self.atlas_list.pop(page_name)

    def display(self) -> None:
        """
        Prints all pages in the Atlas.
        """
        number = 1
        for page_name, object_ in self.atlas_list.items():
            if isinstance(object_, TileSet):
                print(f"[{number}]\tPage name: {page_name}, type: {type(object_)}\n"
                      f"\t\t{object_.tile_list}")
            else:
                print(f"[{number}]\tPage name: {page_name}, type: {type(object_)}\n"
                      f"\t\t{object_}")
            number += 1
