import libtcodpy as tcod


def handle_keys(key):
    input = {
        tcod.KEY_UP: {'move': (0, -1)},
        tcod.KEY_DOWN: {'move': (0, 1)},
        tcod.KEY_LEFT: {'move': (-1, 0)},
        tcod.KEY_RIGHT: {'move': (1, 0)},
        tcod.KEY_ESCAPE: {'exit': True},
        0: {}
    }

    if key.vk == tcod.KEY_ENTER and key.lalt:
        return {'fullscreen': True}
    else:
        try:
            return input[key.vk]
        except KeyError as e:
            return {}
