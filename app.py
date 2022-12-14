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
''')
st.write(r"""
where:
- An = vector representing the value of the balance sheet at time n;
- cn = vector of financial/economic transactions;
- f (.) = linear affine function in both arguments.
""")
st.latex(r'''
\left\{\begin{matrix}
L_{n} = L_{n-1} +\bar{n}_{n}\cdot (T_{n-1}+Z_{n})-\gamma_{n}\cdot K_{n-1}+\bar{\omega }_{n}\cdot (D_{n-1}-G_{n})+d_{n}\cdot B_{n-1}+E_{n}+X_{n}  &  &  &  &  & \\
T_{n}= (1-\bar{n}_{n})\cdot (T_{n-1}+Z_{n})&  &  &  &  & \\ 
R_{n}= \phi_{n}\cdot R_{n-1}+\Delta Q_{n}\cdot V_{n} &  &  &  &  & \\
K_{n}=(1+\gamma_{n}) \cdot K_{n-1} - A_{n}&  &  &  & & \\ 
D_{n}=(1-\bar{\omega }_{n})\cdot(D_{n-1}-G_{n}) &  &  &  &  & \\ 
B_{n}=B_{n-1}-E_{n}
&  &  &  &  & 
\end{matrix}\right.
''')
st.write(r"""
where:
- Ln = Cash and Cash equivalence;
- Tn = Trade receivables;
- Rn = Inventories;
- Kn = Property, Plan and Equipment;
- Dn = Trade and other payables;
- Bn = Long term Borrowings.
""")
df_balancesheet = pd.read_csv(DATA_BALANCESHEET, sep = ';')
df_balancesheet_cleaned= clean_balancesheet(df_balancesheet)
df_balancesheet_cleaned_notnull = df_balancesheet_cleaned.style.highlight_null(props="color: transparent;")
st.dataframe(df_balancesheet_cleaned_notnull)
#https://cicciosar-dragonfly-app-z8xeob.streamlitapp.com