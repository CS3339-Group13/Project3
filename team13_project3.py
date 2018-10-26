import sys
from Disassembler import Disassembler
from WriteBackUnit import WriteBackUnit
from ALU import ALU
from ControlUnit import ControlUnit


class SimplifiedSuperScalarSimulator:

    def __init__(self, inst, data, outfile):
        self.__instructions = inst
        self.__memory = data
        self.__outfile = outfile

        self.__cu = ControlUnit()
        self.__wb = WriteBackUnit()
        self.__alu = ALU()

        # Buffers
        self.__pre_alu = {
            'inst id': None,
            'arg1': None,
            'arg2': None,
            'dest reg': None
        }
        self.__post_mem = {
            'inst id': None,
            'dest reg': None,
            'value': None
        }
        self.__post_alu = {
            'inst id': None,
            'dest reg': None,
            'value': None
        }

    def run(self):
        for inst in self.__instructions:
            control = self.__cu.run(inst)
            self.__wb.run(self.__post_mem, self.__post_alu)
            self.__alu.run(self.__pre_alu, control['alu op'])


if __name__ == "__main__":
    infile = ''
    outfile = ''

    # Get in/out file from command line arguments
    for i in range(len(sys.argv)):
        if sys.argv[i] == '-i':
            infile = sys.argv[i + 1]
        elif sys.argv[i] == '-o':
            outfile = sys.argv[i + 1]

    d = Disassembler(infile, outfile)
    d.run()
    processed_inst = d.get_processed_inst()
    processed_data = d.get_processed_data()

    ssss = SimplifiedSuperScalarSimulator(processed_inst, processed_data, outfile)
    ssss.run()
