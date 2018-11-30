class IssueUnit:

    def __init__(self, register_file):
        self.__register_file = register_file

    def run(self, issue_in):

        type = issue_in['type'].lower()

        if type == 'd':
            return {
                'id': issue_in['id'],
                'rt_val': self.__register_file.read_register(issue_in['rt']),
                'offset': issue_in['offset'],
                'rn_val': self.__register_file.read_register(issue_in['rn']),
                'mem_write': True if issue_in['name'] == 'STUR' else False,
                'assembly': issue_in['assembly']
            }, 'mem'
        else:
            out = {
                'id': issue_in['id'],
                'op': issue_in['name'],
                'rd': issue_in['rd'],
                'shamt_val': None,
                'rn_val': None,
                'rm_val': None,
                'assembly': issue_in['assembly']
            }
            if type == 'i':
                out['imm_val'] = issue_in['immediate']
                out['rn_val'] = self.__register_file.read_register(issue_in['rn'])
            elif type == 'r':
                out['rm_val'] = self.__register_file.read_register(issue_in['rm'])
                out['rn_val'] = self.__register_file.read_register(issue_in['rn'])
                out['shamt'] = issue_in['shamt']
            elif type == 'im':
                out['imm_val'] = issue_in['immediate']
                out['shamt_val'] = issue_in['shamt']
            return out, 'alu'
