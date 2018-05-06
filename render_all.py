import libtcodpy as tcod


class Render(object):
    def __init__(self, con, game_map, SCREEN_WIDTH, SCREEN_HEIGHT, colors):
        self.con = con
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.map = game_map
        self.colors = colors

    def render_all(self, entities):
        for y in range(self.map.height):
            for x in range(self.map.width):
                wall = self.map.tiles[x][y].block_sight

                if wall:
                    tcod.console_set_char_background(
                        self.con, x, y,
                        self.colors.get('dark_wall'),
                        tcod.BKGND_SET)
                else:
                    tcod.console_set_char_background(
                        self.con, x, y,
                        self.colors.get('dark_ground'),
                        tcod.BKGND_SET)

        # draw creatures
        for entity in entities:
            self.draw_entity(entity)

            tcod.console_blit(self.con, 0, 0,
                              self.SCREEN_WIDTH, self.SCREEN_HEIGHT,
                              0, 0, 0)

    def clear_all(self, entities):
        for entity in entities:
            self.clear_entity(entity)

    def draw_entity(self, entity):
        tcod.console_set_default_foreground(self.con, entity.color)
        tcod.console_put_char(self.con, entity.x, entity.y,
                              entity.icon, tcod.BKGND_NONE)

    def clear_entity(self, entity):
        tcod.console_put_char(self.con, entity.x, entity.y,
                              ' ', tcod.BKGND_NONE)
