from time import sleep


class SpecialSymbols:
    euro = chr(128)
    inverted_expl = chr(161)
    cent = chr(162)
    sterling = chr(163)
    spec_symbol_1 = chr(164)
    yuan = chr(165)
    paragraph_1 = chr(167)
    copyright_symbol_1 = chr(169)
    dual_cursor_to_left = chr(171)
    copyright_symbol_2 = chr(174)
    degree = chr(176)
    plus_minus = chr(177)
    prefix_micro = chr(181)
    paragraph_2 = chr(182)
    dual_cursor_to_right = chr(187)
    one_quarter = chr(188)
    one_second = chr(189)
    tree_quarter = chr(190)
    inverted_ques = chr(191)
    multiplication = chr(215)
    spec_symbol_2 = chr(390)
    spec_symbol_3 = chr(391)
    function_symbol = chr(402)
    spec_symbol_4 = chr(404)
    spec_symbol_5 = chr(405)
    spec_symbol_6 = chr(407)
    spec_symbol_7 = chr(408)
    spec_symbol_8 = chr(410)
    spec_symbol_9 = chr(411)
    nu = chr(414)
    theta = chr(415)
    sigma = chr(425)
    pi = chr(426)
    tau = chr(429)
    omega_1 = chr(433)
    gamma = chr(947)
    round_and_point = chr(664)
    cursor_up = chr(708)
    cursor_down = chr(709)
    si_and_point_right = chr(892)
    si_and_point_left = chr(893)
    triangle = chr(916)
    tree_lines = chr(926)
    psi = chr(936)
    omega_2 = chr(937)
    beta = chr(946)
    alpha = chr(945)
    spec_symbol_10 = chr(948)
    epsilon = chr(949)
    lambda_ = chr(955)
    pi_ = chr(960)
    lightning = chr(990)
    spec_symbol_11 = chr(992)
    spec_symbol_12 = chr(993)
    spec_symbol_13 = chr(1146)
    spec_symbol_14 = chr(1148)
    spec_symbol_15 = chr(1149)
    spec_symbol_16 = chr(1150)
    spec_symbol_17 = chr(1151)
    spec_symbol_18 = chr(1152)
    spec_symbol_19 = chr(1154)
    spec_symbol_20 = chr(1160)
    spec_symbol_21 = chr(1161)
    dagger_1 = chr(1421)
    dagger_2 = chr(1422)


class Text:
    class Font:
        Black = "\033[30m"
        Red = "\033[31m"
        Green = "\033[32m"
        Yellow = "\033[33m"
        Blue = "\033[34m"
        Magenta = "\033[35m"
        Cyan = "\033[36m"
        White = "\033[37m"
        Bright_black = "\033[90m"
        Bright_red = "\033[91m"
        Bright_green = "\033[92m"
        Bright_yellow = "\033[93m"
        Bright_blue = "\033[94m"
        Bright_magenta = "\033[95m"
        Bright_cyan = "\033[96m"

    class Back:
        Black = "\033[40m"
        Red = "\033[41m"
        Green = "\033[42m"
        Yellow = "\033[43m"
        Blue = "\033[44m"
        Magenta = "\033[45m"
        Cyan = "\033[46m"
        White = "\033[47m"
        Bright_black = "\033[100m"
        Bright_red = "\033[101m"
        Bright_green = "\033[102m"
        Bright_yellow = "\033[103m"
        Bright_blue = "\033[104m"
        Bright_magenta = "\033[105m"
        Bright_cyan = "\033[106m"

    class Tool:
        Flush = "\033[0m"
        Bold = "\033[1m"
        Cursive = "\033[3m"
        Underline = "\033[4m"
        Strike = "\033[9m"
        Dual_underline = "\033[21m"


tag_styles = \
    {
        "b": Text.Tool.Bold,
        "c": Text.Tool.Cursive,
        "cls": Text.Tool.Flush,
        "s": Text.Tool.Strike,
        "u": Text.Tool.Underline,
        "du": Text.Tool.Dual_underline,
        "fb": Text.Font.Black,
        "fb1": Text.Font.Blue,
        "fr": Text.Font.Red,
        "fc": Text.Font.Cyan,
        "fm": Text.Font.Magenta,
        "fy": Text.Font.Yellow,
        "fg": Text.Font.Green,
        "fw": Text.Font.White,
        "fbb": Text.Font.Bright_black,
        "fbb1": Text.Font.Bright_blue,
        "fbr": Text.Font.Bright_red,
        "fbc": Text.Font.Bright_cyan,
        "fbm": Text.Font.Bright_magenta,
        "fby": Text.Font.Bright_yellow,
        "fbg": Text.Font.Bright_green,
        "bb": Text.Back.Black,
        "bb1": Text.Back.Blue,
        "br": Text.Back.Red,
        "bc": Text.Back.Cyan,
        "bm": Text.Back.Magenta,
        "by": Text.Back.Yellow,
        "bg": Text.Back.Green,
        "bw": Text.Back.White,
        "bbb": Text.Back.Bright_black,
        "bbb1": Text.Back.Bright_blue,
        "bbr": Text.Back.Bright_red,
        "bbc": Text.Back.Bright_cyan,
        "bbm": Text.Back.Bright_magenta,
        "bby": Text.Back.Bright_yellow,
        "bbg": Text.Back.Bright_green
    }


def print_slowly(text__: str, delay=0.21) -> None:
    """
    Print slowly your text with any delay
    :param text__:
    :param delay: float
    :return: None
    """

    for char in text__:
        print(char, end="", flush=True)
        sleep(delay)
    print()


def formated(text__: str) -> str:
    """
    Format your text use tags
    :param text__:
    :return:
    """

    global tag_styles

    formatted_text = ""
    tag_stack = []

    while text__:
        max_tag = ""
        max_tag_len = 0
        for tag in tag_styles.keys():
            if text__.startswith("\\" + tag) and len(tag) > max_tag_len:
                max_tag = tag
                max_tag_len = len(tag)

        if max_tag:
            if max_tag in tag_stack:
                tag_stack.remove(max_tag)
                formatted_text += f"{Text.Tool.Flush}"
            else:
                tag_stack.append(max_tag)
                formatted_text += f"{tag_styles[max_tag]}"
            text__ = text__[len(max_tag) + 1:]
        else:
            formatted_text += text__[0]
            text__ = text__[1:]

    return formatted_text[:-2] + formatted_text[-1] + Text.Tool.Flush


def hex_to_rgb(hex_string: str, to_tuple: bool, to_dictionary: bool) -> dict or tuple:
    """
    Convert from hex to rgb. Include 2 modes:\nconvert final result to tuple or dict
    :param to_dictionary:
    :param hex_string: str
    :param to_tuple: bool    :param to_dictionary:
    :return: dict or tuple
    """

    if to_dictionary is True:
        def for_dict(string: str) -> dict:
            return {'r': int(str(string.lstrip('#'))[0:2], 16),
                    'g': int(str(string.lstrip('#'))[2:4], 16),
                    'b': int(str(string.lstrip('#'))[4:6], 16)}

        return for_dict(hex_string)

    elif to_tuple is True:
        def to_tuple(string: str) -> tuple:
            r = int(string.lstrip('#')[0:2], 16)
            g = int(string.lstrip('#')[2:4], 16)
            b = int(string.lstrip('#')[4:6], 16)
            return r, g, b

        return to_tuple(hex_string)

    else:
        raise TypeError(
            f"Incorrect input {hex_string=}, {to_tuple=} or {to_dictionary=}")


def rgb_to_hex(rgb_color: tuple or dict) -> str:
    """
    Convert from RGB(type of tuple or dict) to Hex
    :param rgb_color: tuple or dict
    :return: str
    """

    if isinstance(rgb_color, tuple):
        def for_tuple(color: tuple) -> str:
            r = color[0]
            g = color[1]
            b = color[2]
            return "#{:02x}{:02x}{:02x}".format(r, g, b).upper()

        return for_tuple(rgb_color)

    elif isinstance(rgb_color, dict):
        def for_dict(color: dict) -> str:
            r = color["r"]
            g = color["g"]
            b = color["b"]
            return "#{:02x}{:02x}{:02x}".format(r, g, b).upper()

        return for_dict(rgb_color)

    else:
        raise TypeError(f"Incorrect value {rgb_color=}")


