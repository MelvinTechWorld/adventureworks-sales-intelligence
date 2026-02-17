import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sales Intelligence Dashboard", layout="wide")

st.title("📊 AdventureWorks Sales Intelligence")

st.write("Executive-level overview of sales performance.")

# Load dataset
sales = pd.read_csv("exports/cleaned_sales.csv")

# KPIs
total_revenue = sales["SalesAmount"].sum()
total_profit = sales["Profit"].sum()
profit_margin = total_profit / total_revenue
aov = total_revenue / sales["SalesOrderNumber"].nunique()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Revenue", f"${total_revenue:,.0f}")
col2.metric("Total Profit", f"${total_profit:,.0f}")
col3.metric("Profit Margin", f"{profit_margin:.0%}")
col4.metric("Avg Order Value", f"${aov:,.0f}")