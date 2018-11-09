class ALU:

    def __init__(self):
        pass

    def run(self, alu_in, control):
        arg1 = alu_in['arg1']  # rn_val
        arg2 = alu_in['arg2']  # rm_val

        op = control['name']
        f = getattr(self, 'op_' + op.lower())

        return {
            'id': alu_in['id'],
            'dest': alu_in['dest'],
            'val': f(arg1, arg2)
        }

    @staticmethod
    def op_and(arg1, arg2):
        return arg1 & arg2

    @staticmethod
    def op_add(arg1, arg2):
        return arg1 + arg2

    @staticmethod
    def op_orr(arg1, arg2):
        return arg1 | arg2

    @staticmethod
    def op_eor(arg1, arg2):
        return arg1 ^ arg2

    @staticmethod
    def op_sub(arg1, arg2):
        return arg1 - arg2

    @staticmethod
    def op_asr(arg1, shamt):
        return arg1 >> shamt

    @staticmethod
    def op_lsr(arg1, shamt):
        return (arg1 % (1 << 32)) >> shamt

    @staticmethod
    def op_lsl(arg1, shamt):
        return arg1 << shamt
