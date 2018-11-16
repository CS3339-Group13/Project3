import sys
from Disassembler import Disassembler
from WriteBackUnit import WriteBackUnit
from ALU import ALU
from MemoryUnit import MemoryUnit
from collections import deque
from RegisterFile import RegisterFile
from Cache import Cache
from IFUnit import IFUnit
from IssueUnit import IssueUnit


class SimplifiedSuperScalarSimulator:
    
    def __init__(self, infile, outfile, num_registers=32):
        self.__input_file = infile
        self.__output_file = outfile

        self.__pc = 96

        self.__memory = {}
        self.__outfile = outfile

        self.__register_file = RegisterFile(num_registers)
        self.__wb = WriteBackUnit(self.__register_file)
        self.__cache = Cache(self.__memory)
        self.__alu = ALU()
        self.__mem = MemoryUnit(self.__cache)
        self.__if = IFUnit(self.__cache)
        self.__iu = IssueUnit()

        self.pre_issue_size = 4
        self.pre_alu_size = 2
        self.pre_mem_size = 2
        self.post_alu_size = 1
        self.post_mem_size = 1

        self.__pre_issue_buffer = deque(maxlen=self.pre_issue_size)

        self.__pre_mem_buffer = deque(maxlen=self.pre_mem_size)
        self.__pre_alu_buffer = deque(maxlen=self.pre_alu_size)

        self.__post_mem_buffer = deque(maxlen=self.post_mem_size)
        self.__post_alu_buffer = deque(maxlen=self.post_alu_size)

        self.__read_file()

    def __read_file(self):
        """
        Reads the designated input file and stores each line as a decimal integer
        """
        pc = 96
        with open(self.__input_file, 'r') as f:
            for line in f:
                line = line.rstrip()
                if len(line) != 32:
                    raise ValueError('ERROR: Invalid instruction on line {}: \'{}\''.format((pc-96)/4, line))
                self.__memory[pc] = int(line, 2)
                pc += 4

    def run(self):
        while self.__pc in self.__memory.keys():
            
            pre_issue_space = self.pre_issue_size - len(self.__pre_issue_buffer)
            pre_alu_space = self.pre_alu_size - len(self.__pre_alu_buffer)
            pre_mem_space = self.pre_mem_size - len(self.__pre_mem_buffer)
            post_alu_space = self.post_alu_size - len(self.__post_alu_buffer)
            post_mem_space = self.post_mem_size - len(self.__post_mem_buffer)

            # Run WriteBackUnit
            if len(self.__post_mem_buffer) > 0:
                wb_in = self.__post_mem_buffer.popleft()
                self.__wb.run(wb_in, 'mem')
            if len(self.__post_alu_buffer) > 0:
                wb_in = self.__post_alu_buffer.popleft()
                self.__wb.run(wb_in, 'alu')

            # Run ALU
            # If pre-buffer not empty and post-buffer not full
            if len(self.__pre_alu_buffer) > 0 and post_alu_space > 0:
                alu_in = self.__pre_alu_buffer.popleft()
                alu_out = self.__alu.run(alu_in)
                self.__post_alu_buffer.append(alu_out)

            # Run MemoryUnit
            # If pre-buffer not empty and post-buffer not full
            if len(self.__pre_mem_buffer) > 0 and post_mem_space > 0:
                mem_in = self.__pre_mem_buffer.popleft()
                mem_out = self.__mem.run(mem_in)
                self.__post_mem_buffer.append(mem_out)

            # Run Issue Unit
            # If pre-buffer not empty
            for x in range(2):
                if len(self.__pre_issue_buffer) > 0:
                    inst = self.__iu.run(self.__pre_issue_buffer.popleft())

                    if pre_alu_space > 0 and inst[1] == 'alu':
                        self.__pre_alu_buffer.append(inst[0])
                        pass
                    if pre_mem_space > 0 and inst[1] == 'mem':
                        self.__pre_mem_buffer.append(inst[0])
                        pass

            # Run IF Unit
            # If pre-issue buffer not full
            if pre_issue_space == 0:
                continue
            elif pre_issue_space == 1:
                self.__pc += 4
                inst = self.__if.run(self.__pc, 1)
                self.__pre_issue_buffer.append(inst)
            else:
                self.__pc += 8
                insts = self.__if.run(self.__pc, 2)
                self.__pre_issue_buffer.append(insts[0])
                self.__pre_issue_buffer.append(insts[1])


if __name__ == "__main__":
    infile = ''
    outfile = ''

    # Get in/out file from command line arguments
    for i in range(len(sys.argv)):
        if sys.argv[i] == '-i':
            infile = sys.argv[i + 1]
        elif sys.argv[i] == '-o':
            outfile = sys.argv[i + 1]

    ssss = SimplifiedSuperScalarSimulator(infile, outfile)
    ssss.run()
