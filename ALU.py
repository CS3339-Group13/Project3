class ALU:

    def __init__(self):
        pass

    # self.__pre_alu = {
    #     'inst id': None,
    #     'arg1': None,
    #     'arg2': None,
    #     'dest reg': None
    # }
    def run(self, pre, op):
        f = getattr(self, 'op_' + op.lower())

        return {
            'inst id': pre['inst id'],
            'dest reg': pre['dest reg'],
            'value': f()
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
