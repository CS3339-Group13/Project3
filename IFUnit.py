from Disassembler import Disassembler


class IFUnit:

    def __init__(self, cache):
        self.__cache = cache

    def run(self, pc, num_inst):
        try:
            insts = self.__cache.read(pc)
        except KeyError:
            return False

        if not insts:
            return pc
        elif num_inst == 1:
            out = Disassembler.process(insts[0]) if pc % 8 == 0 else Disassembler.process(insts[1])
            out['id'] = (pc - 96) / 4
            return out
        else:
            out1 = Disassembler.process(insts[0])
            out1['id'] = (pc - 96) / 4
            out2 = Disassembler.process(insts[1])
            out2['id'] = (pc - 96) / 4 + 4
            return out1, out2

