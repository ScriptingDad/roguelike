class Rect(object):
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h

    def center(self):
        x = (self.x1 + self.x2) // 2
        y = (self.y1 + self.y2) // 2
        return (x, y)

    def intersect(self, other):
        return (self.x1 <= other.x2 and self.x2 >= other.x1
                and self.y1 <= other.y2 and self.y2 >= other.y1)

    def __repr__(self):
        return ('Starting Point: {}, {}, End Point: {}, {};'
                ' Center {}, {}').format(self.x1,
                                         self.y1,
                                         self.x2,
                                         self.y2,
                                         self.center()[0],
                                         self.center()[1])


class GameMap(object):
    levels = []

    def __init__(self, console):
        self.console = console

    #
    # def init_tiles(self):
    #
    #

    def create_room(room, game_map):
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                game_map[x][y].blocked = False
                game_map[x][y].block_sight = False

    def create_h_tunnel(self, x1, x2, y, level):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            self.levels[level][x][y].blocked = False
            self.levels[level][x][y].block_sight = False
        return (x, y)

    def create_v_tunnel(y1, y2, x, game_map):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            game_map[x][y].blocked = False
            game_map[x][y].block_sight = False
        return (x, y)


def render_all(objs, game_map, con):
    for obj in objs:
        obj.draw()

    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            wall = game_map[x][y].blocked
            if wall:
                tcod.console_set_char_background(con, x, y, COLOR_DARK_WALL,
                                                 tcod.BKGND_SET)
            else:
                tcod.console_set_char_background(con, x, y, COLOR_DARK_GROUND,
                                                 tcod.BKGND_SET)
    tcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)
