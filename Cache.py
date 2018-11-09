class Cache:

    def __init__(self):
        block = {
            'valid': False,
            'dirty': False,
            'tag': None,
            'content': (None, None)
        }

        set = {
            'lru': False,
            'blocks': (block, block)
        }

        self.__cache = (set, set, set, set)
