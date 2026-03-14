import numpy as np

def croston_forecast(demand):

    demand = np.array(demand)

    non_zero = demand[demand > 0]

    if len(non_zero) == 0:
        return 0

    avg_demand = np.mean(non_zero)

    avg_interval = len(demand) / len(non_zero)

    forecast = avg_demand / avg_interval

    return forecast