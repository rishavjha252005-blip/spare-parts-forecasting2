import numpy as np

def ses_forecast(demand, alpha=0.3):

    demand = np.array(demand)

    forecast = demand[0]

    for actual in demand[1:]:

        forecast = alpha * actual + (1 - alpha) * forecast

    return forecast