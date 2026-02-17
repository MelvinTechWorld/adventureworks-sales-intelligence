# 📊 AdventureWorks Sales Intelligence Dashboard

## 🔎 Project Overview

This project analyzes AdventureWorks sales data to uncover revenue trends, profitability drivers, customer behavior patterns, and regional performance insights.

Using Python (Pandas, Scikit-learn, Matplotlib) for data analysis and Tableau Public for executive visualization, the goal was to simulate a real-world end-to-end sales intelligence workflow.

---

## 🎯 Business Objectives

- Identify overall revenue and profit performance
- Analyze profitability across regions
- Track monthly sales trends (2005–2008)
- Identify top-performing products
- Segment customers using RFM analysis
- Apply KMeans clustering for behavioral grouping
- Build a simple monthly sales forecasting model

---

## 📊 Executive Dashboard Insights

### 🔑 Key KPIs

- **Total Revenue:** $29M  
- **Total Profit:** $12M  
- **Profit Margin:** 41%  
- **Average Order Value:** $1,061  

### 🌍 Regional Performance

- North America leads both revenue and profitability.
- Pacific and Europe show similar revenue levels but slightly lower profit contribution.

### 📈 Monthly Trend

Sales grew significantly toward 2008, indicating strong upward momentum.

---

## 🧠 Advanced Analytics

### RFM Segmentation
Customers were segmented based on:
- Recency
- Frequency
- Monetary Value

Segments include:
- VIP
- Loyal
- At Risk
- Regular

### KMeans Clustering
- Standardized RFM features
- Used Elbow Method to determine optimal clusters
- Visualized clusters using PCA

### Sales Forecasting
- Aggregated monthly sales
- Added lag features
- Built regression model
- Reduced forecasting error through feature engineering

---

## 🛠 Tech Stack

**Data Processing & Analysis**
- Python
- Pandas
- NumPy

**Machine Learning**
- Scikit-learn (StandardScaler, KMeans)

**Visualization**
- Matplotlib
- Tableau Public

---

## 📌 Key Takeaways

- Revenue growth accelerated in 2008.
- North America drives the strongest profit contribution.
- A small number of premium products generate significant revenue.
- Feature engineering significantly improved forecasting accuracy.

---

## 💡 Future Improvements

- Implement ARIMA or Prophet for forecasting
- Add time-series cross-validation
- Deploy interactive Streamlit dashboard
- Connect to live database instead of static CSV files