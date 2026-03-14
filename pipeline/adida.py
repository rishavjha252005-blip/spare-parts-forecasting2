import numpy as np

def adida_aggregate(demand, period=7):

    demand = np.array(demand)

    n = len(demand)

    n_trim = n - (n % period)

    demand = demand[:n_trim]

    aggregated = demand.reshape(-1, period).sum(axis=1)

    return aggregated