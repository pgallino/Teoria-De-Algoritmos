
class NegativeCycleResult:

    def __init__(self, found, message, cycle="", weight=0):
        self.found = found
        self.message = message
        self.cycle = cycle
        self.weight = weight