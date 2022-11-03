import streamlit as st
import pandas as pd
#import plotly.express as px

DATA_BALANCESHEET = "balance_sheet.csv"

#ENDER_COLS = ["INDUSTRY CODE DESC", "ANNUAL REVENUE DEDUCTION FACTOR"]

# DASHBOARD
st.title("BALANCE SHEET BASED MODEL FOR CREDIT RISK")
st.write("The model allows to compute the default boundary level based on book value quantities. It is able to link the Credit Risk Literatute with the Financial Statement Analysis.")




st.write("Mathematically speaking, we introduce in the call payoff defining the value of the Equity with the presence of the liquidity shortage, the stochastic liquidity process and the stochastic debt process.")
st.latex(r'''
    A_{n}=
    \f(A_{n-1},c_{n})
    ''')

df_balancesheet = pd.read_csv(DATA_BALANCESHEET)
#https://cicciosar-dragonfly-app-z8xeob.streamlitapp.com