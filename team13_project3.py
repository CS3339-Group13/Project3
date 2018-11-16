import sys
from Disassembler import Disassembler
from WriteBackUnit import WriteBackUnit
from ALU import ALU
from MemoryUnit import MemoryUnit
from Queue import Queue
from RegisterFile import RegisterFile
from Cache import Cache
from IFUnit import IFUnit


class SimplifiedSuperScalarSimulator:

    def __init__(self, inst, data, outfile, num_registers=32):
        self.__pc = 96

        self.__instructions = inst
        self.__memory = data
        self.__outfile = outfile

        self.__register_file = RegisterFile(num_registers)
        self.__wb = WriteBackUnit(self.__register_file)
        self.__cache = Cache(self.__memory)
        self.__alu = ALU()
        self.__mem = MemoryUnit(self.__cache)
        self.__if = IFUnit(self.__pc, self.__instructions, self.__cache)

        # Buffers
        self.__pre_issue_buffer = Queue(maxsize=4)

        self.__pre_mem_buffer = Queue(maxsize=2)

        # arg1, arg2
        self.__pre_alu_buffer = Queue(maxsize=2)

        # inst id, value, dest
        self.__post_mem_buffer = Queue(maxsize=1)

        # inst id, value
        self.__post_alu_buffer = Queue(maxsize=1)

    def run(self):
        inst = None
        while self.__pc in self.__instructions.keys():

            # Run WriteBackUnit
            if not self.__post_mem_buffer.empty() or not self.__post_alu_buffer.empty():
                wb_in = (self.__post_mem_buffer.get(), self.__post_alu_buffer.get())
                self.__wb.run(wb_in)

            # Run ALU
            if not self.__pre_alu_buffer.empty():
                alu_in = self.__pre_alu_buffer.get()
                alu_out = self.__alu.run(alu_in)
                self.__post_alu_buffer.put(alu_out)

            # Run MemoryUnit
            if not self.__pre_mem_buffer.empty():
                mem_in = self.__pre_mem_buffer.get()
                mem_out = self.__mem.run(mem_in)
                self.__post_mem_buffer.put(mem_out)

            # Run Issue Unit

            # Run IF Unit




    def __read_cache(self, addr):
        pass


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
