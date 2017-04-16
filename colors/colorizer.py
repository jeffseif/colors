def Colorizer(color, weight=1):
    """Function for bash-style color formatting."""
    def inner(value):
        return template.format(value)

    template = '\033[{:d};{:d}m{{:s}}\033[0m'.format(weight, color)
    return inner
