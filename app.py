import streamlit as st
import pandas as pd
import plotly.express as px

#DATA = "data.csv"
#ENDER_COLS = ["INDUSTRY CODE DESC", "ANNUAL REVENUE DEDUCTION FACTOR"]

# DASHBOARD
st.title("CLIMATE REVENUE DISCOUNT FACTORS")
st.write("Factors show the annual increase of company costs measured as percent of industry revenues driven by the carbon price increase. Calculated according to the formula below")
st.latex(r'''
    \delta = \frac{\text{Industry GHG Emissions(tn)} \times \text{ETS Price(USD/tn)}}{\text{Industry Output, USD}} \times \text{Tax rate}
    ''')
st.write("Tax rate assumed to be 10%, which is the carbon price increase compatible with the 1.5 degree goal")

st.header('Discount Factors per industry and country')
