class WriteBackUnit:

    def __init__(self):
        pass

    def run(self, wb_in):

        inst_id = wb_in[0]['id']
        dest1 = wb_in[0]['dest']
        value1 = wb_in[0]['value']

        dest2 =  wb_in[1]['dest']
        value2 = wb_in[1]['value']

        return {
            'dest1': dest1,
            'value1': value1,
            'dest2': dest2,
            'value2': value2
        }
