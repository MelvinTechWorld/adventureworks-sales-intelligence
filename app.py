import streamlit as st
import pandas as pd
import plotly.express as px
import os

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="AdventureWorks Sales Intelligence",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------
@st.cache_data
def load_data():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(BASE_DIR, "exports", "cleaned_sales.csv")

    sales = pd.read_csv(data_path)

    # Clean column names just in case
    sales.columns = sales.columns.str.strip()

    # Convert date column
    sales["FullDateAlternateKey"] = pd.to_datetime(
        sales["FullDateAlternateKey"]
    )

    return sales

sales = load_data()

# --------------------------------------------------
# KPI CALCULATIONS
# --------------------------------------------------
total_revenue = sales["SalesAmount"].sum()
total_profit = sales["Profit"].sum()
profit_margin = total_profit / total_revenue
avg_order_value = total_revenue / sales["SalesOrderNumber"].nunique()

# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.title("📊 AdventureWorks Sales Intelligence")
st.markdown("Executive-level overview of sales performance.")

# --------------------------------------------------
# KPI SECTION
# --------------------------------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Revenue", f"${total_revenue:,.0f}")
col2.metric("Total Profit", f"${total_profit:,.0f}")
col3.metric("Profit Margin", f"{profit_margin:.0%}")
col4.metric("Avg Order Value", f"${avg_order_value:,.0f}")

st.divider()

# --------------------------------------------------
# REVENUE BY REGION
# --------------------------------------------------
st.subheader("Revenue by Region")

region_revenue = (
    sales.groupby("SalesTerritoryGroup")["SalesAmount"]
    .sum()
    .reset_index()
)

fig_region = px.bar(
    region_revenue,
    x="SalesAmount",
    y="SalesTerritoryGroup",
    orientation="h",
    text_auto=".2s",
)

st.plotly_chart(fig_region, use_container_width=True)

# --------------------------------------------------
# PROFIT BY REGION
# --------------------------------------------------
st.subheader("Profit by Region")

region_profit = (
    sales.groupby("SalesTerritoryGroup")["Profit"]
    .sum()
    .reset_index()
)

fig_profit = px.bar(
    region_profit,
    x="Profit",
    y="SalesTerritoryGroup",
    orientation="h",
    text_auto=".2s",
)

st.plotly_chart(fig_profit, use_container_width=True)

# --------------------------------------------------
# MONTHLY REVENUE TREND
# --------------------------------------------------
st.subheader("Monthly Revenue Trend")

monthly_sales = (
    sales
    .groupby(pd.Grouper(key="FullDateAlternateKey", freq="M"))
    ["SalesAmount"]
    .sum()
    .reset_index()
)

fig_monthly = px.line(
    monthly_sales,
    x="FullDateAlternateKey",
    y="SalesAmount"
)

st.plotly_chart(fig_monthly, use_container_width=True)

# --------------------------------------------------
# TOP 10 PRODUCTS
# --------------------------------------------------
st.subheader("Top 10 Products by Revenue")

top_products = (
    sales.groupby("EnglishProductName")["SalesAmount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig_top = px.bar(
    top_products,
    x="SalesAmount",
    y="EnglishProductName",
    orientation="h",
    text_auto=".2s",
)

st.plotly_chart(fig_top, use_container_width=True)