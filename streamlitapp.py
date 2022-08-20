import streamlit as st
import pandas as pd

st.selectbox('Pick one', ['CandA', 'CandB'])
df = pd.read_excel("ID.xlsx")
print(df)
