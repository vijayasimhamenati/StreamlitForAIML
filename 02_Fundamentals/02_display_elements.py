import streamlit as st 
import pandas as pd 

df = pd.read_csv("02_data.csv")
st.dataframe(df)

st.write(df)

st.table(df)

# metric 

st.metric(label = "Temperature", value = "46 C",delta = -5 )