class Colors:
    orange = (244,116,17)
    yellow = (237,234, 4)
    purple = (166,0,247)
    cyan = (21, 204, 209)
    blue = (13, 64, 216)
    dark_grey = (26,31,40)
    green = (47,230,23)
    red = (232,18,18)
    white = (255,255,255)
    dark_blue = (44,44,127)
    light_blue = (59,85,162)

    @classmethod #class level self
    def get_cell_colors(cls):
        return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]