from enum import Enum
from typing import Final

__all__ = [
    "Color",
    "styled_string",
]

STYLE_BASE: Final[str] = "\033[{}m"


class Color(str, Enum):
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    MAGENTA = 35
    CYAN = 36
    LIGHT_GRAY = 37
    GRAY = 90
    LIGHT_RED = 91
    LIGHT_GREEN = 92
    LIGHT_YELLOW = 93
    LIGHT_BLUE = 94
    LIGHT_MAGENTA = 95
    LIGHT_CYAN = 96
    WHITE = 97


def styled_string(
    string: str,
    foregroundColor: Color | None = None,
    backgroundColor: Color | None = None,
    bold: bool = False,
    italic: bool = False,
    underline: bool = False,
) -> str:
    new_string = string

    if foregroundColor:
        new_string = STYLE_BASE.format(foregroundColor.value) + new_string
    if backgroundColor:
        new_string = STYLE_BASE.format(backgroundColor.value + 10) + new_string
    if bold:
        new_string = STYLE_BASE.format(1) + new_string
    if italic:
        new_string = STYLE_BASE.format(3) + new_string
    if underline:
        new_string = STYLE_BASE.format(4) + new_string

    return new_string + STYLE_BASE.format(0)
