class WriteBackUnit:

    def __init__(self):
        pass

    def run(self, post_mem, post_alu):
        r1 = post_mem['dest reg']
        val1 = post_mem['value']
        r2 = post_alu['dest reg']
        val2 = post_mem['value']

        # Write to registers???
