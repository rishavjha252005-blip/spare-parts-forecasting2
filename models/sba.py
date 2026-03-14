import numpy as np

def sba_forecast(demand):

    demand = np.array(demand)

    non_zero = demand[demand > 0]

    if len(non_zero) == 0:
        return 0

    avg_demand = np.mean(non_zero)

    avg_interval = len(demand) / len(non_zero)

    croston = avg_demand / avg_interval

    alpha = 0.1

    forecast = croston * (1 - alpha/2)

    return forecast