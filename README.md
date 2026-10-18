# ✈️ SkyNest — Airline Delay Analysis Using Apache Spark

## 📌 Project Overview

SkyNest is a Big Data Analytics project that analyzes airline flight delays using Apache Spark and presents the results through an interactive Streamlit dashboard.

The project aims to explore airline performance, identify airports with higher delay rates, and understand monthly flight delay patterns through data processing and visualization.

The dashboard provides an intuitive interface for exploring flight statistics and comparing delay trends across airlines and airports.

## 🎯 Objectives

- Analyze airline flight delay data using Apache Spark.
- Calculate total flights and delayed flights.
- Examine delay rates across different airlines.
- Compare airport performance based on flight delays.
- Analyze monthly flight delay trends.
- Present analytical results through interactive visualizations.

## 🛠️ Technologies Used

- **Apache Spark (PySpark)** — Distributed data processing and analysis.
- **Python** — Data processing and application development.
- **Pandas** — Data manipulation and analysis.
- **Streamlit** — Interactive dashboard development.
- **Plotly** — Interactive charts and visualizations.
- **GitHub** — Version control and project hosting.
- **Streamlit Community Cloud** — Dashboard deployment.

## 📊 Dashboard Features

### 1. Flight Statistics
Displays key performance indicators, including:
- Total number of flights.
- Number of delayed flights.
- Overall flight delay rate.

### 2. Airline Analysis
Visualizes and compares flight delay performance across airlines.

### 3. Airport Analysis
Examines airport-level delay patterns to identify airports with higher delay rates.

### 4. Monthly Delay Trends
Displays monthly trends to help explore changes in flight delays over time.

### 5. Interactive Visualizations
Provides interactive charts and tables to make the analysis easier to explore and understand.

## 📁 Project Structure

```text
airline-delay-analysis/
│
├── app.py
├── requirements.txt
├── README.md
│
└── outputs/
    ├── airline_results/
    │   └── part-*.csv
    │
    ├── airport_results/
    │   └── part-*.csv
    │
    └── monthly_results/
        └── part-*.csv
