
class MaxFlowMinCostResult:

    def __init__(self, success=True, flow=0, cost=0):
        self.success = success
        self.message = "Cantidad de personas maxima: " + str(flow) + " - Costo minimo: " + str(cost)
        self.flow = flow
        self.cost = cost