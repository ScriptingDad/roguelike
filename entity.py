import libtcodpy as tcod


class Entity(object):
    def __init__(self, x, y, icon, color=tcod.white):
        self.x = x
        self.y = y
        self.icon = icon
        self.color = color

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
