def inventory_decision(mean_demand, std_dev):

    service_factor = 1.65

    safety_stock = service_factor * std_dev

    reorder_point = mean_demand + safety_stock

    return safety_stock, reorder_point