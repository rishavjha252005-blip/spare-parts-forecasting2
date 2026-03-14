from models.ses import ses_forecast
from models.croston import croston_forecast
from models.sba import sba_forecast


def select_model(demand_type):

    if demand_type == "Smooth":
        return "SES"

    elif demand_type == "Erratic":
        return "SBA"

    elif demand_type == "Intermittent":
        return "Croston"

    elif demand_type == "Lumpy":
        return "Croston + Bootstrapping"

    else:
        return "SES"


def run_forecast(model, demand):

    if model == "SES":

        return ses_forecast(demand)

    elif model == "SBA":

        return sba_forecast(demand)

    elif model == "Croston":

        return croston_forecast(demand)

    elif model == "Croston + Bootstrapping":

        return croston_forecast(demand)

    else:

        return demand.mean()