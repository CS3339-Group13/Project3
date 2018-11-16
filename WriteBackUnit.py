class WriteBackUnit:

    def __init__(self, register_file):
        self.__register_file = register_file

    def run(self, wb_in):

        # Post-Mem
        id1 = wb_in[0]['id']
        dest1 = wb_in[0]['rn']
        value1 = wb_in[0]['value']

        # Post-ALU
        id2 = wb_in[1]['id']
        dest2 = wb_in[1]['rd']
        value2 = wb_in[1]['value']

        self.__register_file.write_register(dest1, value1)
        self.__register_file.write_register(dest2, value2)
