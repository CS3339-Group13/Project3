class IssueUnit:

    def __init__(self):
        pass

    def run(self, issue_in):

        type = issue_in['type']

        if type == 'd':
            return {
                'id': issue_in['id'],
                'rt': issue_in['rt'],
                'offset': issue_in['offset'],
                'rn': issue_in['rn'],
                'mem_write': True if issue_in['name'] == 'STUR' else False
            }, 'mem'
        else:
            out = {
                'id': issue_in['id'],
                'op': issue_in['name'],
                'rd': issue_in['rd']
            }
            if type == 'i':
                out['imm'] = issue_in['immediate']
                out['rn'] = issue_in['rn']
            elif type == 'r':
                out['rm'] = issue_in['rm']
                out['rn'] = issue_in['rn']
                out['shamt'] = issue_in['shamt']
            elif type == 'im':
                out['shamt'] = issue_in['shamt']
                out['imm'] = issue_in['immediate']
            return out, 'alu'
