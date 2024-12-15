from PIL import Image
import numpy as np
import os


def ascii_pixel(r: int, g: int, b: int, sign: str = " ") -> str:
    """
    Generates a string to display a pixel in the terminal with a specified background and character.

    :param r: int - red color value (0-255)
    :param g: int - green color value (0-255)
    :param b: int - blue color value (0-255)
    :param sign: str - character to be displayed (default is a space)
    :return: str - string with ANSI code for colored background and character
    """
    return f"\033[48;2;{r};{g};{b}m {sign} \033[0m"


def PrintImg2Terminal(image_path__: str, cell_mode: int = 0) -> str or None:
    """
    Converts an image into a terminal format using colored backgrounds for each pixel.

    :param image_path__: str - path to the image to be displayed
    :param cell_mode: int - character display mode (0-5):
        0 - space (default),
        1 - dot,
        2 - plus,
        3 - star,
        4 - 'x',
        5 - exclamation mark
    :return: str or None - string with the image in terminal format or None in case of an error
    """

    term_picture: str = ""

    if not os.path.exists(image_path__):
        print(f"File not found: {image_path__}")
    else:
        try:
            img_array = np.array(Image.open(image_path__).convert("RGB"))

            # Determine the character based on the mode
            sign_: str = " "
            if cell_mode == 1:
                sign_ = "."
            elif cell_mode == 2:
                sign_ = "+"
            elif cell_mode == 3:
                sign_ = "*"
            elif cell_mode == 4:
                sign_ = "x"
            elif cell_mode == 5:
                sign_ = "!"

            # Build the string for the terminal
            for row in img_array:
                term_picture += f"{''.join(ascii_pixel(r, g, b, sign_) for r, g, b in row)}\n"
            return term_picture
        except Exception as e:
            print(f"Error preparing the image: {e}")


class TermArt:
    def __init__(self, path_for_picture: str) -> None:
        self.path: str = path_for_picture
        self.art: str = ""

    def __str__(self) -> str:
        return self.art

    def __del__(self) -> None:
        del self.art, self.path

    def upload(self, cell_sign: str = " ", convert_format: str = "RGB") -> None:
        img_array = np.array(Image.open(self.path).convert(convert_format.upper()))
        for row in img_array:
            self.art += f"{''.join(ascii_pixel(r, g, b, cell_sign) for r, g, b in row)}\n"

    def delete(self) -> None:
        self.art: str = ""
        self.path: str = ""

    def reInit(self, path_for_picture: str) -> None:
        self.path = path_for_picture

    def sizes(self) -> tuple[int]:
        width, height = Image.open(self.path).width, Image.open(self.path).height
        return width, height
