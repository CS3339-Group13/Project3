class MemoryUnit:

    def __init__(self):
        pass

    def run(self, mem_in, op):
        if op['mem_write']:
            self.__store(mem_in)
        else:
            self.__load(mem_in)

    def __store(self):
        pass

    def __load(self):
        pass
