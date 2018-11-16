class MemoryUnit:

    def __init__(self, cache):
        self.__cache = cache

    def run(self, mem_in):
        if mem_in['mem_write']:
            self.__store(mem_in)
            return {
                'id': mem_in['id'],
                'rn': None,
                'value': None
            }
        else:
            return {
                'id': mem_in['id'],
                'rn': mem_in['rn'],
                'value': self.__load(mem_in)
            }

    def __store(self, mem_in):
        id = mem_in['id']
        rt = mem_in['rt']
        offset = mem_in['offset']
        rn = mem_in['rn']

        self.__cache.write(rt + offset, rn)

    def __load(self, mem_in):
        id = mem_in['id']
        rt = mem_in['rt']
        offset = mem_in['offset']

        return self.__cache.read(rt + offset)
