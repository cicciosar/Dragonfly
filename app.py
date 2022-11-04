import streamlit as st
import pandas as pd
import numpy as np
#import plotly.express as px

DATA_BALANCESHEET = "balance_sheet.csv"

#ENDER_COLS = ["INDUSTRY CODE DESC", "ANNUAL REVENUE DEDUCTION FACTOR"]

#Function to clean the balance sheet from na values
def clean_balancesheet(df):
    for i in df.columns:
        df[i].replace(['n.d.'],None,)
    return df



# DASHBOARD
st.title("BALANCE SHEET BASED MODEL FOR CREDIT RISK")
st.write("The model allows to compute the default boundary level based on book value quantities. It is able to link the Credit Risk Literatute with the Financial Statement Analysis.")

st.write("Mathematically speaking, we introduce in the call payoff defining the value of the Equity with the presence of the liquidity shortage, the stochastic liquidity process and the stochastic debt process.")
st.latex(r'''

A_{n}=f(A_{n-1},c_{n}),

\\where:
\\An= vector representing the value of the balance sheet at time n;
\\cn = vector of financial/economic transactions; 
\\f (.)= linear affine function in both arguments.
    ''')


df_balancesheet = pd.read_csv(DATA_BALANCESHEET, sep = ';')
df_balancesheet_cleaned= clean_balancesheet(df_balancesheet)
df_balancesheet_cleaned_notnull = df_balancesheet_cleaned.style.highlight_null(props="color: transparent;")
st.dataframe(df_balancesheet_cleaned_notnull)
#https://cicciosar-dragonfly-app-z8xeob.streamlitapp.com