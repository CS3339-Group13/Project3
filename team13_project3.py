import sys
from Disassembler import Disassembler
from WriteBackUnit import WriteBackUnit
from ALU import ALU
from MemoryUnit import MemoryUnit
from ControlUnit import ControlUnit
from Queue import Queue


class SimplifiedSuperScalarSimulator:

    def __init__(self, inst, data, outfile, num_registers=32):
        self.__pc = 96

        self.__instructions = inst
        self.__memory = data
        self.__outfile = outfile

        self.__cu = ControlUnit()
        self.__wb = WriteBackUnit()
        self.__alu = ALU()
        self.__mem = MemoryUnit()

        self.__register_file = [0] * num_registers

        # Buffers
        self.__pre_issue_buffer = Queue()

        self.__pre_mem_buffer = Queue()

        # arg1, arg2
        self.__pre_alu_buffer = Queue()

        # inst id, value, dest
        self.__post_mem_buffer = Queue()

        # inst id, value
        self.__post_alu_buffer = Queue()

    def run(self):
        for inst in self.__instructions:

            # Get control signals
            control = self.__cu.run(inst)

            # Run WriteBackUnit
            wb_in = (self.__post_mem_buffer.get(), self.__post_alu_buffer.get())
            wb_out = self.__wb.run(wb_in)
            self.__write_register(wb_out['dest1'], wb_out['value1'])
            self.__write_register(wb_out['dest2'], wb_out['value2'])

            # Run ALU
            alu_in = self.__pre_alu_buffer.get()
            alu_out = self.__alu.run(alu_in, control)
            self.__post_alu_buffer.put(alu_out)

            # Run MemoryUnit
            mem_in = self.__pre_mem_buffer.get()
            mem_out = self.__mem.run(mem_in, control)
            self.__post_mem_buffer.put(mem_out)

            # Run Issue Unit

            # Run IF Unit



    def __write_register(self, r, val):
        if r is None or val is None:
            pass
        self.__register_file[r] = val

    def __read_cache(self, addr):



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
