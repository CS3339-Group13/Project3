class ControlUnit:

    def __init__(self):
        pass

    @staticmethod
    def run(inst):
        return {
            'alu op': inst['name']
        }
