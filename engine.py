from random import randint

import libtcodpy as tcod

from entity import Entity
from input_handler import handle_keys
from render_all import Render
from map_objects.game_map import GameMap

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
LIMIT_FPS = 20

MAP_WIDTH = 80
MAP_HEIGHT = 45

COLOR_DARK_WALL = tcod.Color(0, 0, 100)
COLOR_DARK_GROUND = tcod.Color(50, 50, 150)

ROOM_MAX_SIZE = 10
ROOM_MIN_SIZE = 6
MAX_ROOMS = 30


def main():
    tcod.console_set_custom_font(
        'arial10x10.png',
        tcod.FONT_TYPE_GRAYSCALE | tcod.FONT_LAYOUT_TCOD
    )
    tcod.console_init_root(
        SCREEN_WIDTH,
        SCREEN_HEIGHT,
        'RogueLike Tutorial',
        False
    )
    con = tcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)

    colors = {
        'dark_wall': tcod.Color(0, 0, 50),
        'dark_ground': tcod.Color(50, 50, 150),
    }

    game_map = GameMap(width=MAP_WIDTH, height=MAP_HEIGHT)
    renderer = Render(con, game_map, SCREEN_WIDTH, SCREEN_HEIGHT, colors)

    pc = Entity(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, '@')
    npc = Entity(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, '@', tcod.yellow)
    entities = [pc, npc]

    while not tcod.console_is_window_closed():
        tcod.console_set_default_foreground(con, tcod.white)
        renderer.render_all(entities)
        tcod.console_flush()
        renderer.clear_all(entities)

        key = tcod.console_wait_for_keypress(False)
        action = handle_keys(key)
        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move and not game_map.is_blocked(pc.x + move[0], pc.y + move[1]):
            pc.move(*move)

        if exit:
            return True

        if fullscreen:
            tcod.console_set_fullscreen(not tcod.console_is_fullscreen)


if __name__ == '__main__':
    print('Starting game:')
    main()
