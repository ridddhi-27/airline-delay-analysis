# ✈️ SkyNest — Airline Delay Analysis Using Apache Spark

## 📌 Project Overview

SkyNest is a Big Data Analytics project that analyzes airline flight delays using Apache Spark and presents the results through an interactive Streamlit dashboard.

The project focuses on analyzing flight delay patterns across airlines and airports and exploring monthly trends. It uses Apache Spark for data processing and Plotly visualizations to present the results in an interactive and user-friendly dashboard.

The dashboard helps users explore flight statistics, compare airline performance, identify airports with higher delay rates, and understand changes in delays over time.

## 🎯 Project Objectives

- Analyze airline flight data using Apache Spark.
- Calculate the total number of flights and delayed flights.
- Analyze flight delay rates across different airlines.
- Compare flight delay patterns across airports.
- Explore monthly trends in flight delays.
- Create an interactive dashboard for visualizing analytical results.
- Demonstrate the application of Big Data Analytics to the aviation domain.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Apache Spark (PySpark) | Large-scale data processing and analysis |
| Pandas | Data manipulation and analysis |
| Streamlit | Interactive dashboard development |
| Plotly | Interactive charts and visualizations |
| GitHub | Source code management |
| Streamlit Community Cloud | Dashboard deployment |

## 📊 Dashboard Features

### 1. Flight Statistics

Displays key performance indicators, including:

- Total number of flights.
- Number of delayed flights.
- Overall flight delay rate.

### 2. Airline Analysis

Visualizes airline-level delay statistics to help compare delay performance across different airlines.

### 3. Airport Analysis

Examines airport-level delay statistics to identify airports with comparatively higher flight delay rates.

### 4. Monthly Delay Trends

Displays monthly flight delay trends to help users explore changes in flight delays over time.

### 5. Interactive Visualizations

Provides interactive charts and data tables through a Streamlit dashboard, making the analytical results easier to explore and understand.

## 📁 Project Structure

The repository is organized as follows:

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
```

### File Description

- `app.py` — Contains the Streamlit dashboard code.
- `requirements.txt` — Lists the Python dependencies required to run the dashboard.
- `README.md` — Provides project documentation and setup instructions.
- `airline_results/` — Stores the aggregated airline analysis results.
- `airport_results/` — Stores the aggregated airport analysis results.
- `monthly_results/` — Stores the aggregated monthly analysis results.

The CSV files contain the previously generated analytical results produced by the Spark workflow.

## ⚙️ Installation and Setup

Follow these steps to run the dashboard on your local machine.

### Prerequisites

Make sure you have the following installed:

- Python 3.9 or a compatible Python version.
- pip package manager.
- Git (optional, for cloning the repository).

### Step 1: Clone the Repository

Open a terminal or command prompt and run:

```bash
git clone https://github.com/riddhi-27/airline-delay-analysis.git
```

### Step 2: Navigate to the Project Directory

```bash
cd airline-delay-analysis
```

### Step 3: Install the Required Dependencies

Run the following command:

```bash
pip install -r requirements.txt
```

### Step 4: Run the Streamlit Dashboard

Execute:

```bash
streamlit run app.py
```

The dashboard will open in your web browser.

**Note:** The dashboard reads the saved CSV analysis results from the `outputs/` directory. The Spark analysis must be executed separately to regenerate those results.

## 📦 Dependencies

The dashboard requires the following Python libraries:

```text
streamlit
pandas
plotly
```

These dependencies are listed in `requirements.txt` and can be installed using pip.

Apache Spark (PySpark) is used during the data processing and analysis stage. It is not required to run the dashboard if the precomputed CSV output files are already available.

## 🔄 Project Workflow

The project follows these major steps:

1. **Data Collection:** Obtain the airline flight dataset.
2. **Data Preparation:** Prepare the dataset for analysis.
3. **Big Data Processing:** Use Apache Spark to process the flight data.
4. **Data Analysis:** Calculate flight statistics and analyze delays across airlines, airports, and months.
5. **Result Storage:** Save the aggregated analytical results as CSV files.
6. **Data Visualization:** Load the CSV results into the Streamlit dashboard.
7. **Interactive Exploration:** Present the results through charts, metrics, and tables.
8. **Deployment:** Deploy the dashboard using Streamlit Community Cloud.

## 👩‍💻 Team Members

This project was developed as part of the Big Data Analytics (BDA) Lab.

| Team Member | Responsibility |
|---|---|
| Riddhi | Dataset, Airport Analysis & Visualization |
| Vaidehi | Apache Spark Implementation |

## 🌟 Expected Outcomes

The project aims to provide:

- A better understanding of airline flight delay patterns.
- Comparisons of delay performance across airlines.
- Insights into airport-level delay statistics.
- An overview of monthly flight delay trends.
- An interactive dashboard for presenting analytical findings.
- Practical experience with Apache Spark and data visualization tools.

## 🔮 Future Enhancements

Possible future improvements include:

- Adding more factors that may contribute to flight delays.
- Incorporating weather and seasonal information.
- Adding interactive filters for airlines, airports, and time periods.
- Exploring machine learning models for flight delay prediction.
- Improving the dashboard with additional visualizations.
- Expanding the analysis to include more datasets.

## 📌 Conclusion

SkyNest demonstrates the use of Apache Spark for airline flight data analysis and Streamlit for interactive data visualization.

By combining Big Data processing with interactive charts and statistical summaries, the project provides a convenient way to explore airline performance, airport delay patterns, and monthly flight delay trends.

The project illustrates how data analytics can help transform large datasets into meaningful visual insights.

---

**Project Title:** Airline Delay Analysis Using Apache Spark  
**Domain:** Big Data Analytics  
**Programming Language:** Python  
**Data Processing:** Apache Spark (PySpark)  
**Dashboard:** Streamlit and Plotly  
**Repository:** [airline-delay-analysis](https://github.com/riddhi-27/airline-delay-analysis)
