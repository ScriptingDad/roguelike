from libtcodpy import Color


class Tile(object):
    """
    A tile on a map.  It may or may not be blocked and may or may not
    block sights.
    """

    def __init__(self, blocked, block_sight=None):
        self.blocked = blocked

        if block_sight is None:
            block_sight = blocked

        self.block_sight = block_sight
