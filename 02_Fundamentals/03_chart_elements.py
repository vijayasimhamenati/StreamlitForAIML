import streamlit as st 
import pandas as pd 

df = pd.read_csv("02_data.csv")

st.line_chart(df, x= "HireDate", y= "Salary"  )
st.bar_chart(df, x= "FirstName", y= "Salary"  )
st.area_chart(df,x="FirstName", y= ["Salary","Loan"],color= ["#fd0", "#f0f"])