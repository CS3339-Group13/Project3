import sys
from Disassembler import Disassembler
from WriteBackUnit import WriteBackUnit


# Buffer design


class SimplifiedSuperScalarSimulator:

    def __init__(self, inst, data, outfile):
        self.__instructions = inst
        self.__memory = data
        self.__outfile = outfile

        self.__wb = WriteBackUnit()

        self.__post_mem = {

        }
        self.__post_alu = {

        }

    def run(self):
        self.__wb.pull(self.__post_mem, self.__post_alu)


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
