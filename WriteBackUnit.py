class WriteBackUnit:

    def __init__(self, register_file):
        self.__register_file = register_file

    def run(self, wb_in, source):

        if source == 'mem':
            id = wb_in[0]['id']
            dest = wb_in[0]['rn']
            value = wb_in[0]['value']
        else:
            id = wb_in[1]['id']
            dest = wb_in[1]['rd']
            value = wb_in[1]['value']

        self.__register_file.write_register(dest, value)
