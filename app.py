import os
import glob
import pandas as pd
import streamlit as st
import plotly.express as px


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="SkyNest | Airline Delay Analysis",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# COLORS
# =========================================================

BG = "#F8F7FB"
WHITE = "#FFFFFF"
PLUM = "#302344"
DARK_PLUM = "#241A36"
PURPLE = "#8D72C7"
LAVENDER = "#EAE1F5"
PASTEL_BLUE = "#E0E9FA"
PASTEL_MINT = "#DDEFE5"
TEXT = "#302B3A"
MUTED = "#777181"
BORDER = "#EAE5F0"


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');

    .stApp {{
        background: {BG};
        color: {TEXT};
        font-family: 'DM Sans', sans-serif;
    }}

    /* SIDEBAR */
    [data-testid="stSidebar"] {{
        background: {DARK_PLUM};
        border-right: 1px solid #413450;
    }}

    [data-testid="stSidebar"] * {{
        color: #F7F2FC;
    }}

    [data-testid="stSidebar"] .stMultiSelect label {{
        color: #F7F2FC !important;
    }}

    [data-testid="stSidebar"] [data-baseweb="tag"] {{
        background-color: {PURPLE};
    }}

    [data-testid="stSidebar"] .stCaption {{
        color: #C9BED8 !important;
    }}

    /* SIDEBAR COLLAPSE / REOPEN ARROW */
    [data-testid="collapsedControl"],
    [data-testid="stSidebarCollapsedControl"] {{
        display: flex !important;
        visibility: visible !important;
        opacity: 1 !important;
        pointer-events: auto !important;
        position: fixed !important;
        top: 10px !important;
        left: 10px !important;
        z-index: 9999999 !important;
        background-color: #EAE1F5 !important;
        border-radius: 8px !important;
    }}

    [data-testid="stSidebarCollapseButton"] {{
        display: flex !important;
        visibility: visible !important;
        opacity: 1 !important;
    }}

    [data-testid="stHeader"] {{
        background: transparent;
    }}

    /* GENERAL LAYOUT */
    h1, h2, h3 {{
        font-family: 'Manrope', sans-serif !important;
        color: {PLUM};
    }}

    .block-container {{
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1500px;
    }}

    #MainMenu {{
        visibility: hidden;
    }}

    footer {{
        visibility: hidden;
    }}

    /* HERO BANNER */
    .hero {{
        background: linear-gradient(
            120deg,
            #EEE6F8 0%,
            #F6F0FA 52%,
            #E6EDF9 100%
        );
        border: 1px solid #E5DCEF;
        border-radius: 24px;
        padding: 35px 38px;
        margin-bottom: 27px;
        position: relative;
        overflow: hidden;
    }}

    .hero::after {{
        content: "✈";
        position: absolute;
        right: 42px;
        top: 2px;
        font-size: 115px;
        color: rgba(141, 114, 199, 0.15);
        transform: rotate(-12deg);
    }}

    .hero-eyebrow {{
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 2px;
        color: #7E65AD;
        margin-bottom: 13px;
    }}

    .hero-title {{
        font-family: 'Manrope', sans-serif;
        font-size: 35px;
        line-height: 1.2;
        font-weight: 800;
        color: {PLUM};
        margin-bottom: 12px;
        position: relative;
        z-index: 1;
    }}

    .hero-description {{
        font-size: 14px;
        line-height: 1.8;
        color: #6F667D;
        max-width: 680px;
        position: relative;
        z-index: 1;
    }}

    .hero-badge {{
        display: inline-block;
        background: rgba(255,255,255,0.72);
        border: 1px solid #E3D9F0;
        border-radius: 30px;
        padding: 7px 13px;
        font-size: 11px;
        color: #71569D;
        margin-top: 17px;
        font-weight: 700;
    }}

    /* SECTION HEADINGS */
    .section-heading {{
        font-family: 'Manrope', sans-serif;
        font-size: 21px;
        font-weight: 800;
        color: {PLUM};
        margin-top: 14px;
        margin-bottom: 4px;
    }}

    .section-description {{
        font-size: 12px;
        color: {MUTED};
        margin-bottom: 15px;
    }}

    /* KPI CARDS */
    .kpi-card {{
        background: {WHITE};
        border: 1px solid {BORDER};
        border-radius: 18px;
        padding: 21px 22px;
        min-height: 135px;
        box-shadow: 0 4px 18px rgba(54, 35, 76, 0.035);
    }}

    .kpi-label {{
        color: {MUTED};
        font-size: 12px;
        font-weight: 600;
        margin-bottom: 13px;
    }}

    .kpi-value {{
        font-family: 'Manrope', sans-serif;
        font-size: 30px;
        font-weight: 800;
        color: {PLUM};
        line-height: 1.2;
    }}

    .kpi-note {{
        color: {MUTED};
        font-size: 11px;
        margin-top: 9px;
    }}

    .kpi-icon {{
        float: right;
        width: 38px;
        height: 38px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 19px;
    }}

    .card-lavender .kpi-icon {{
        background: {LAVENDER};
    }}

    .card-blue .kpi-icon {{
        background: {PASTEL_BLUE};
    }}

    .card-mint .kpi-icon {{
        background: {PASTEL_MINT};
    }}

    /* CHARTS */
    div[data-testid="stPlotlyChart"] {{
        background: {WHITE};
        border: 1px solid {BORDER};
        border-radius: 18px;
        padding: 8px;
        box-shadow: 0 4px 18px rgba(54, 35, 76, 0.025);
    }}

    /* TABLES */
    div[data-testid="stExpander"] {{
        background: {WHITE};
        border: 1px solid {BORDER};
        border-radius: 13px;
    }}

    div[data-testid="stDataFrame"] {{
        border: 1px solid {BORDER};
        border-radius: 12px;
        overflow: hidden;
    }}

    /* SIDEBAR BRAND */
    .sidebar-brand {{
        font-family: 'Manrope', sans-serif;
        font-size: 25px;
        font-weight: 800;
        color: #FFFFFF;
        margin-top: 12px;
    }}

    .sidebar-subtitle {{
        font-size: 11px;
        letter-spacing: 1.5px;
        color: #C7B8DB;
        margin-bottom: 26px;
    }}

    .sidebar-divider {{
        border-top: 1px solid #51405F;
        margin: 23px 0;
    }}

    .sidebar-info {{
        background: #352844;
        border: 1px solid #4B3B5A;
        border-radius: 14px;
        padding: 14px;
        color: #E5DCEE;
        font-size: 12px;
        line-height: 1.7;
    }}

    /* FOOTER */
    .footer {{
        text-align: center;
        color: #948B9F;
        font-size: 11px;
        padding: 28px 0 5px 0;
    }}

    @media (max-width: 768px) {{
        .hero {{
            padding: 25px 22px;
        }}

        .hero-title {{
            font-size: 27px;
        }}

        .hero::after {{
            right: 10px;
            font-size: 70px;
        }}

        .kpi-value {{
            font-size: 24px;
        }}
    }}

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# FUNCTION TO LOAD SPARK CSV FILES
# =========================================================

def load_spark_csv(folder):
    """Load Spark part-*.csv files from a folder."""

    if not os.path.isdir(folder):
        return pd.DataFrame()

    csv_files = sorted(
        glob.glob(os.path.join(folder, "part-*.csv"))
    )

    if not csv_files:
        return pd.DataFrame()

    frames = []

    for file in csv_files:
        try:
            df = pd.read_csv(file)

            if not df.empty:
                frames.append(df)

        except Exception as error:
            st.warning(f"Could not read {file}: {error}")

    if not frames:
        return pd.DataFrame()

    result = pd.concat(frames, ignore_index=True)
    result.columns = result.columns.astype(str).str.strip()

    return result


# =========================================================
# LOAD DATA
# =========================================================

airline_df = load_spark_csv("outputs/airline_results")
airport_df = load_spark_csv("outputs/airport_results")
monthly_df = load_spark_csv("outputs/monthly_results")
# =========================================================
# VALIDATE OUTPUT FILES
# =========================================================

missing_folders = []

if airline_df.empty:
    missing_folders.append("outputs/airline_results")

if airport_df.empty:
    missing_folders.append("outputs/airport_results")

if monthly_df.empty:
    missing_folders.append("outputs/monthly_results")

if missing_folders:
    st.error("Analysis output files are missing or empty.")

    for folder in missing_folders:
        st.code(folder)

    st.info(
        "Run your Spark analysis first. Each folder should contain "
        "Spark part-*.csv files."
    )

    st.stop()


# =========================================================
# VALIDATE REQUIRED COLUMNS
# =========================================================

required_columns = [
    "total_flights",
    "delayed_flights_15min_plus",
    "delay_rate_percent"
]

missing_columns = [
    col for col in required_columns
    if col not in airline_df.columns
]

if missing_columns:
    st.error(
        "Missing airline columns: " + ", ".join(missing_columns)
    )
    st.write(
        "Available airline columns:",
        airline_df.columns.tolist()
    )
    st.stop()


if "delay_rate_percent" not in airport_df.columns:
    st.error("Airport output is missing delay_rate_percent.")
    st.write(
        "Available airport columns:",
        airport_df.columns.tolist()
    )
    st.stop()


if "delay_rate_percent" not in monthly_df.columns:
    st.error("Monthly output is missing delay_rate_percent.")
    st.write(
        "Available monthly columns:",
        monthly_df.columns.tolist()
    )
    st.stop()


if "year_month" not in monthly_df.columns:
    st.error("Monthly output is missing year_month.")
    st.write(
        "Available monthly columns:",
        monthly_df.columns.tolist()
    )
    st.stop()


# =========================================================
# PREPARE DATA
# =========================================================

for col in required_columns:
    airline_df[col] = pd.to_numeric(
        airline_df[col],
        errors="coerce"
    )

airport_df["delay_rate_percent"] = pd.to_numeric(
    airport_df["delay_rate_percent"],
    errors="coerce"
)

monthly_df["delay_rate_percent"] = pd.to_numeric(
    monthly_df["delay_rate_percent"],
    errors="coerce"
)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        """
        <div class="sidebar-brand">✈ SkyNest</div>
        <div class="sidebar-subtitle">AVIATION ANALYTICS</div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### Dashboard Controls")

    st.caption(
        "Explore flight delays across airlines, airports, and months."
    )

    st.markdown(
        '<div class="sidebar-divider"></div>',
        unsafe_allow_html=True
    )

    st.markdown("#### Analysis Filters")

    st.caption("Filters apply to the airline chart.")

    st.markdown(
        '<div class="sidebar-divider"></div>',
        unsafe_allow_html=True
    )

    st.markdown("#### About this project")

    st.markdown(
        """
        <div class="sidebar-info">
        <b>Airline Delay Analysis</b><br><br>
        A data analytics project using Apache Spark to analyze flight delays
        and visualize patterns across airlines, airports, and time periods.
        <br><br>
        <b>Technology</b><br>
        Apache Spark · Python · Pandas · Plotly · Streamlit
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.caption("BDA LAB PROJECT")


# =========================================================
# HERO BANNER
# =========================================================

st.markdown(
    """
<div class="hero">
<div class="hero-eyebrow">AVIATION INTELLIGENCE · FLIGHT OPERATIONS</div>
<div class="hero-title">Understanding Flight Delays</div>
<div class="hero-description">
Explore airline performance, identify airports with higher
departure delay rates, and uncover monthly trends through
interactive visual analytics powered by Apache Spark.
</div>
<div class="hero-badge">✦ BIG DATA ANALYTICS</div>
</div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# KPI CALCULATIONS
# =========================================================

total_flights = int(
    airline_df["total_flights"].fillna(0).sum()
)

delayed_flights = int(
    airline_df["delayed_flights_15min_plus"].fillna(0).sum()
)

delay_rate = (
    delayed_flights / total_flights * 100
    if total_flights > 0
    else 0
)


# =========================================================
# KPI SECTION
# =========================================================

st.markdown(
    '<div class="section-heading">Overview at a Glance</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    'A summary of flight activity and departure delays in the dataset.'
    '</div>',
    unsafe_allow_html=True
)

kpi1, kpi2, kpi3 = st.columns(3, gap="medium")


with kpi1:
    st.markdown(
        f"""
        <div class="kpi-card card-lavender">
        <div class="kpi-icon">✈️</div>
        <div class="kpi-label">TOTAL FLIGHTS</div>
        <div class="kpi-value">{total_flights:,}</div>
        <div class="kpi-note">Flights included in the analysis</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with kpi2:
    st.markdown(
        f"""
        <div class="kpi-card card-blue">
        <div class="kpi-icon">⏱️</div>
        <div class="kpi-label">DELAYED FLIGHTS</div>
        <div class="kpi-value">{delayed_flights:,}</div>
        <div class="kpi-note">Departure delays of 15+ minutes</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with kpi3:
    st.markdown(
        f"""
        <div class="kpi-card card-mint">
        <div class="kpi-icon">📊</div>
        <div class="kpi-label">DEPARTURE DELAY RATE</div>
        <div class="kpi-value">{delay_rate:.2f}%</div>
        <div class="kpi-note">Delayed flights as a share of all flights</div>
        </div>
        """,
        unsafe_allow_html=True
    )


st.markdown("<br>", unsafe_allow_html=True)


# =========================================================
# AIRLINE FILTER
# =========================================================

airline_column = airline_df.columns[0]

airline_options = sorted(
    airline_df[airline_column]
    .dropna()
    .astype(str)
    .unique()
    .tolist()
)

with st.sidebar:
    if airline_options:
        selected_airlines = st.multiselect(
            "Select airlines",
            options=airline_options,
            default=airline_options[:min(10, len(airline_options))],
            help="Select airlines to update the airline chart."
        )
    else:
        selected_airlines = []


filtered_airlines = airline_df[
    airline_df[airline_column].astype(str).isin(selected_airlines)
].copy()
# ============================================================
# AIRLINE PERFORMANCE AND AIRPORT INSIGHTS
# ============================================================

airline_section, airport_section = st.columns(2, gap="large")


# ============================================================
# AIRLINE PERFORMANCE
# ============================================================

with airline_section:

    st.markdown(
        """
        <div class="section-heading">
            <h2>✈️ Airline Performance</h2>
            <p>Compare departure delay rates across airlines.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    if filtered_airlines.empty:

        st.warning(
            "No airline data is available for the selected filters."
        )

    else:

        airline_chart_df = filtered_airlines.copy()

        airline_chart_df["delay_rate_percent"] = pd.to_numeric(
            airline_chart_df["delay_rate_percent"],
            errors="coerce"
        )

        airline_chart_df["total_flights"] = pd.to_numeric(
            airline_chart_df["total_flights"],
            errors="coerce"
        )

        airline_chart_df["delayed_flights_15min_plus"] = pd.to_numeric(
            airline_chart_df["delayed_flights_15min_plus"],
            errors="coerce"
        )

        airline_chart_df = airline_chart_df.dropna(
            subset=["delay_rate_percent"]
        )

        airline_chart_df = airline_chart_df.sort_values(
            "delay_rate_percent",
            ascending=False
        )

        if airline_chart_df.empty:

            st.warning(
                "There is no valid delay-rate data to display."
            )

        else:

            fig_airline = px.bar(
                airline_chart_df,
                x=airline_column,
                y="delay_rate_percent",
                color="delay_rate_percent",
                color_continuous_scale=[
                    "#DCD0F0",
                    "#B7A1DD",
                    "#8D72C7"
                ],
                hover_data={
                    "total_flights": True,
                    "delayed_flights_15min_plus": True,
                    "delay_rate_percent": ":.2f"
                },
                title="Departure Delay Rate by Airline",
                labels={
                    airline_column: "Airline",
                    "delay_rate_percent": "Delay Rate (%)",
                    "total_flights": "Total Flights",
                    "delayed_flights_15min_plus": "Delayed Flights"
                }
            )

            fig_airline.update_layout(
                template="plotly_white",
                paper_bgcolor="#FFFFFF",
                plot_bgcolor="#FFFFFF",
                font=dict(
                    family="Arial",
                    size=12,
                    color="#302344"
                ),
                title=dict(
                    text="Departure Delay Rate by Airline",
                    font=dict(
                        size=17,
                        color="#302344"
                    ),
                    x=0.02
                ),
                margin=dict(
                    l=20,
                    r=20,
                    t=65,
                    b=90
                ),
                xaxis=dict(
                    title=dict(
                        text="Airline",
                        font=dict(color="#302344")
                    ),
                    tickfont=dict(color="#302344"),
                    tickangle=-35,
                    showgrid=False,
                    zeroline=False
                ),
                yaxis=dict(
                    title=dict(
                        text="Delay Rate (%)",
                        font=dict(color="#302344")
                    ),
                    tickfont=dict(color="#302344"),
                    ticksuffix="%",
                    gridcolor="#EAE5F0",
                    zeroline=False
                ),
                coloraxis_colorbar=dict(
                    title=dict(
                        text="Delay Rate",
                        font=dict(color="#302344")
                    ),
                    tickfont=dict(color="#302344")
                )
            )

            fig_airline.update_traces(
                marker_line_width=0
            )

            st.plotly_chart(
                fig_airline,
                use_container_width=True,
                config={"displayModeBar": False}
            )

            with st.expander("📋 View airline data"):

                st.dataframe(
                    airline_chart_df,
                    use_container_width=True,
                    hide_index=True
                )


# ============================================================
# AIRPORT INSIGHTS
# ============================================================

with airport_section:

    st.markdown(
        """
        <div class="section-heading">
            <h2>🛫 Airport Insights</h2>
            <p>Identify airports with the highest departure delay rates.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    airport_candidates = [
        "ORIGIN",
        "origin",
        "Origin",
        "airport",
        "Airport",
        "airport_code",
        "origin_airport",
        "ORIGIN_AIRPORT"
    ]

    airport_column = next(
        (
            column
            for column in airport_candidates
            if column in airport_df.columns
        ),
        airport_df.columns[0]
    )

    airport_chart_df = airport_df.copy()

    airport_chart_df["delay_rate_percent"] = pd.to_numeric(
        airport_chart_df["delay_rate_percent"],
        errors="coerce"
    )

    airport_chart_df = airport_chart_df.dropna(
        subset=[
            "delay_rate_percent",
            airport_column
        ]
    )

    airport_chart_df = airport_chart_df.sort_values(
        "delay_rate_percent",
        ascending=False
    ).head(15)

    if airport_chart_df.empty:

        st.warning(
            "No valid airport delay-rate data is available."
        )

    else:

        fig_airport = px.bar(
            airport_chart_df,
            x=airport_column,
            y="delay_rate_percent",
            color="delay_rate_percent",
            color_continuous_scale=[
                "#D7E4F8",
                "#A9C4ED",
                "#7599D5"
            ],
            hover_data={
                "delay_rate_percent": ":.2f"
            },
            title="Top 15 Airports by Departure Delay Rate",
            labels={
                airport_column: "Airport",
                "delay_rate_percent": "Delay Rate (%)"
            }
        )

        fig_airport.update_layout(
            template="plotly_white",
            paper_bgcolor="#FFFFFF",
            plot_bgcolor="#FFFFFF",
            font=dict(
                family="Arial",
                size=12,
                color="#302344"
            ),
            title=dict(
                text="Top 15 Airports by Departure Delay Rate",
                font=dict(
                    size=17,
                    color="#302344"
                ),
                x=0.02
            ),
            margin=dict(
                l=20,
                r=20,
                t=65,
                b=90
            ),
            xaxis=dict(
                title=dict(
                    text="Airport",
                    font=dict(color="#302344")
                ),
                tickfont=dict(color="#302344"),
                tickangle=-35,
                showgrid=False,
                zeroline=False
            ),
            yaxis=dict(
                title=dict(
                    text="Delay Rate (%)",
                    font=dict(color="#302344")
                ),
                tickfont=dict(color="#302344"),
                ticksuffix="%",
                gridcolor="#EAE5F0",
                zeroline=False
            ),
            coloraxis_colorbar=dict(
                title=dict(
                    text="Delay Rate",
                    font=dict(color="#302344")
                ),
                tickfont=dict(color="#302344")
            )
        )

        fig_airport.update_traces(
            marker_line_width=0
        )

        st.plotly_chart(
            fig_airport,
            use_container_width=True,
            config={"displayModeBar": False}
        )

        with st.expander("📋 View airport data"):

            st.dataframe(
                airport_chart_df,
                use_container_width=True,
                hide_index=True
            )
# ============================================================
# MONTHLY DELAY TRENDS
# ============================================================

st.markdown("---")

st.markdown(
    """
    <div class="section-heading">
        <h2>📈 Monthly Delay Trends</h2>
        <p>Track how airline departure delays change over time.</p>
    </div>
    """,
    unsafe_allow_html=True
)

if monthly_df.empty:

    st.warning(
        "Monthly results are unavailable. "
        "Please check the outputs/monthly_results folder."
    )

else:

    monthly_chart_df = monthly_df.copy()

    monthly_chart_df["delay_rate_percent"] = pd.to_numeric(
        monthly_chart_df["delay_rate_percent"],
        errors="coerce"
    )

    monthly_chart_df = monthly_chart_df.dropna(
        subset=["year_month", "delay_rate_percent"]
    )

    monthly_chart_df["year_month"] = (
        monthly_chart_df["year_month"].astype(str)
    )

    monthly_chart_df = monthly_chart_df.sort_values(
        "year_month"
    )

    if monthly_chart_df.empty:

        st.warning(
            "No valid monthly delay data is available to display."
        )

    else:

        fig_monthly = px.line(
            monthly_chart_df,
            x="year_month",
            y="delay_rate_percent",
            markers=True,
            color_discrete_sequence=["#8D72C7"],
            hover_data={
                "delay_rate_percent": ":.2f"
            },
            title="Monthly Departure Delay Rate",
            labels={
                "year_month": "Month",
                "delay_rate_percent": "Delay Rate (%)"
            }
        )

        fig_monthly.update_traces(
            line=dict(
                width=3,
                color="#8D72C7"
            ),
            marker=dict(
                size=8,
                color="#8D72C7",
                line=dict(
                    width=1,
                    color="#FFFFFF"
                )
            ),
            hovertemplate=(
                "<b>Month:</b> %{x}<br>"
                "<b>Delay Rate:</b> %{y:.2f}%"
                "<extra></extra>"
            )
        )

        # Explicit dark-plum formatting for all chart text
        fig_monthly.update_layout(
            template="plotly_white",
            paper_bgcolor="#FFFFFF",
            plot_bgcolor="#FFFFFF",
            font=dict(
                family="Arial",
                size=12,
                color="#302344"
            ),
            title=dict(
                text="Monthly Departure Delay Rate",
                font=dict(
                    size=18,
                    color="#302344"
                ),
                x=0.02
            ),
            margin=dict(
                l=25,
                r=25,
                t=65,
                b=45
            ),
            hoverlabel=dict(
                bgcolor="#FFFFFF",
                font=dict(
                    color="#302344"
                ),
                bordercolor="#EAE5F0"
            ),
            xaxis=dict(
                title=dict(
                    text="Month",
                    font=dict(color="#302344")
                ),
                tickfont=dict(color="#302344"),
                showgrid=False,
                zeroline=False,
                automargin=True
            ),
            yaxis=dict(
                title=dict(
                    text="Delay Rate (%)",
                    font=dict(color="#302344")
                ),
                tickfont=dict(color="#302344"),
                ticksuffix="%",
                gridcolor="#EAE5F0",
                zeroline=False
            )
        )

        st.plotly_chart(
            fig_monthly,
            use_container_width=True,
            config={"displayModeBar": False}
        )

        # Monthly data table
        with st.expander("📋 View monthly data"):

            st.dataframe(
                monthly_chart_df,
                use_container_width=True,
                hide_index=True
            )

# ============================================================
# PROJECT FOOTER
# ============================================================

st.markdown(
    """
    <div style="
        margin-top: 45px;
        padding: 24px 10px;
        text-align: center;
        border-top: 1px solid #EAE5F0;
    ">
        <div style="
            color: #302344;
            font-size: 20px;
            font-weight: 700;
            margin-bottom: 8px;
        ">
            ✈️ SkyNest
        </div>

        <div style="
            color: #777181;
            font-size: 13px;
            line-height: 1.8;
        ">
            Airline Delay Analysis Using Apache Spark
            <br>
            Built with Python, Apache Spark, Streamlit and Plotly
            <br>
            BDA Lab Project
        </div>

        <div style="
            color: #8D72C7;
            font-size: 12px;
            margin-top: 12px;
        ">
            Turning flight data into meaningful insights 💜
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
