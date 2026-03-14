import numpy as np

def bootstrap_simulation(demand, simulations=1000, lead_time=7):

    demand = np.array(demand)

    results = []

    for i in range(simulations):

        sample = np.random.choice(demand, size=lead_time, replace=True)

        results.append(np.sum(sample))

    results = np.array(results)

    mean_demand = np.mean(results)

    std_dev = np.std(results)

    return results, mean_demand, std_dev