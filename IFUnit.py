class IFUnit:

    def __init__(self, pc, instructions, cache):
        self.__instructions = instructions
        self.__cache = cache
        self.__pc = pc

    def run(self):
        insts = self.__cache.read(self.__pc)
