from Disassembler import Disassembler


class IFUnit:

    def __init__(self, cache):
        self.__cache = cache

    def run(self, pc, num_inst):
        try:
            insts = self.__cache.read(pc)
        except KeyError:
            return False

        # If cache miss
        if not insts:
            return False
        else:
            if num_inst == 1:
                if insts[0] == Disassembler.break_inst:
                    return False
                else:
                    out = Disassembler.process(insts[0]) if pc % 8 == 0 else Disassembler.process(insts[1])
                    out['id'] = (pc - 96) / 4
                    return out
            else:
                out1 = Disassembler.process(insts[0])
                out1['id'] = (pc - 96) / 4
                out2 = Disassembler.process(insts[1])
                out2['id'] = (pc - 96) / 4 + 1

                if insts[0] == Disassembler.break_inst:
                    return False
                elif insts[1] == Disassembler.break_inst:
                    return out1,
                else:
                    return out1, out2

