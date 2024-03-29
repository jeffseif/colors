import typing


def Colorizer(color: int, weight: int = 1) -> typing.Callable[[str], str]:
    """Function for bash-style color formatting."""

    def inner(value: str) -> str:
        return template.format(value)

    template = "\033[{:d};{:d}m{{:s}}\033[0m".format(weight, color)
    return inner


RED = Colorizer(31)
GREEN = Colorizer(32)
YELLOW = Colorizer(33)
BLUE = Colorizer(34)
PURPLE = Colorizer(35)
WHITE = Colorizer(37)
GRAY = Colorizer(90)
DARK_RED = Colorizer(31, 0)
DARK_GREEN = Colorizer(32, 0)
DARK_YELLOW = Colorizer(33, 0)
DARK_BLUE = Colorizer(34, 0)
DARK_PURPLE = Colorizer(35, 0)
DARK_WHITE = Colorizer(37, 0)
DARK_GRAY = Colorizer(90, 0)
