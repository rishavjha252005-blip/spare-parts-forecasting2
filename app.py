import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from pipeline.classification import classify_demand
from pipeline.adida import adida_aggregate
from pipeline.forecast_engine import select_model, run_forecast
from pipeline.risk_simulation import bootstrap_simulation
from pipeline.inventory import inventory_decision

st.set_page_config(layout="wide")

st.title("Hybrid Spare Parts Forecasting System")

uploaded_file = st.file_uploader("Upload Dataset", type="csv")

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    df["date"] = pd.to_datetime(df["date"])

    part = st.selectbox("Select Spare Part", df["part_id"].unique())

    data = df[df["part_id"] == part]

    demand = data["demand"].values

    st.subheader("Demand Pattern")

    fig, ax = plt.subplots()

    ax.plot(data["date"], demand, marker="o")

    ax.set_xlabel("Date")
    ax.set_ylabel("Demand")

    st.pyplot(fig)

    demand_type, ADI, CV2 = classify_demand(demand)

    st.write("Demand Type:", demand_type)

    st.write("ADI:", round(ADI,2))

    st.write("CV²:", round(CV2,2))

    model = select_model(demand_type)

    st.write("Recommended Model:", model)

    use_adida = st.checkbox("Use ADIDA aggregation")

    if use_adida:

        demand_used = adida_aggregate(demand)

    else:

        demand_used = demand

    if st.button("Run Forecast"):

        forecast = run_forecast(model, demand_used)

        st.session_state.forecast = forecast

    if "forecast" in st.session_state:

        st.metric("Forecast Demand", round(st.session_state.forecast,2))

    if st.button("Run Risk Simulation"):

        simulations, mean_demand, std_dev = bootstrap_simulation(demand_used)

        st.session_state.simulations = simulations

        st.session_state.mean_demand = mean_demand

        st.session_state.std_dev = std_dev

    if "simulations" in st.session_state:

        fig2, ax2 = plt.subplots()

        ax2.hist(st.session_state.simulations, bins=30)

        ax2.set_title("Demand Risk Distribution")

        st.pyplot(fig2)

    if st.button("Generate Inventory Decision"):

        safety_stock, reorder_point = inventory_decision(

            st.session_state.mean_demand,

            st.session_state.std_dev

        )

        st.session_state.safety_stock = safety_stock

        st.session_state.reorder_point = reorder_point

    if "safety_stock" in st.session_state:

        col1, col2 = st.columns(2)

        col1.metric("Safety Stock", round(st.session_state.safety_stock,2))

        col2.metric("Reorder Point", round(st.session_state.reorder_point,2))