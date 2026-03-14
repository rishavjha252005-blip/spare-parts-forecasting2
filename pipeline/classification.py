import numpy as np

def classify_demand(demand):

    demand = np.array(demand)

    non_zero = demand[demand > 0]

    if len(non_zero) == 0:
        return "No Demand", 0, 0

    ADI = len(demand) / len(non_zero)

    CV2 = (np.std(non_zero) / np.mean(non_zero)) ** 2

    if ADI <= 1.32 and CV2 <= 0.49:
        demand_type = "Smooth"

    elif ADI <= 1.32 and CV2 > 0.49:
        demand_type = "Erratic"

    elif ADI > 1.32 and CV2 <= 0.49:
        demand_type = "Intermittent"

    else:
        demand_type = "Lumpy"

    return demand_type, ADI, CV2