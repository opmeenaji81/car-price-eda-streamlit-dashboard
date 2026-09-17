
import streamlit as st

from utils import load_data


st.set_page_config(
    page_title="Conclusion",
    layout="wide"
)


# -----------------------------
# Load Data
# -----------------------------

df = load_data()


# -----------------------------
# Title
# -----------------------------

st.title("Conclusion")

st.markdown("""
The exploratory data analysis provided an understanding
of the distribution of cars, their characteristics,
and the variation in used-car prices across different
categories and locations.

The following conclusions summarize the areas examined
through the EDA visualizations.
""")


st.divider()


# -----------------------------
# Dataset Overview
# -----------------------------

st.subheader("Dataset Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Cars Analyzed",
        f"{len(df):,}"
    )

with col2:
    st.metric(
        "Average Car Price",
        f"{df['Price'].mean():.2f} Lakhs"
    )

with col3:
    st.metric(
        "Car Companies",
        f"{df['Company_name'].nunique():,}"
    )


st.divider()


# -----------------------------
# Car Characteristics
# -----------------------------

st.subheader("Car Characteristics")

st.markdown("""
- The dataset contains cars from multiple manufacturers.
- Different fuel types are represented, allowing
  comparisons of their distribution.
- Both manual and automatic transmission cars are
  included in the dataset.
- Cars vary in manufacturing year, kilometers driven,
  mileage, engine capacity, and power.
- The company and owner-type charts provide an overview
  of the composition of the available car listings.
""")


st.divider()


# -----------------------------
# Location Insights
# -----------------------------

st.subheader("Location Insights")

st.markdown("""
- The number of car listings varies across locations.
- The location analysis identifies the locations with
  the highest number of listings.
- Average selling prices can also be compared across
  locations.
- These comparisons help explore geographical
  differences in the available used-car listings.
""")


st.divider()


# -----------------------------
# Price Analysis
# -----------------------------

st.subheader("Price Analysis")

st.markdown("""
- The price distribution visualization shows how
  used-car prices are spread across the dataset.
- Average prices can be compared across different
  fuel types.
- The transmission analysis allows comparison of
  average prices between manual and automatic cars.
- These comparisons help identify differences in
  observed prices across vehicle categories.
""")


st.divider()


# -----------------------------
# Relationship Between Variables
# -----------------------------

st.subheader("Relationship Between Variables")

st.markdown("""
The interactive scatter plot allows users to examine
relationships between numerical variables.

The available variables include:

- Manufacturing year
- Kilometers driven
- Mileage
- Engine capacity
- Power
- Selling price

By selecting different variables for the X-axis and
Y-axis, users can visually explore patterns, trends,
and possible relationships in the dataset.
""")


st.divider()


# -----------------------------
# Overall Conclusion
# -----------------------------

st.subheader("Overall Conclusion")

st.markdown("""
The EDA demonstrates that the used-car dataset contains
variation in vehicle characteristics, listing locations,
and selling prices.

The visualizations provide a way to explore:

- Differences in price across fuel types
- Differences in average price by transmission
- Variation in listings across locations
- Differences between car manufacturers
- Relationships between numerical vehicle attributes
  and selling price

The analysis provides an exploratory understanding
of the dataset. The observed patterns can be used
as a starting point for further statistical analysis
or the development of a car price prediction model.
""")


st.divider()


# -----------------------------
# Limitations
# -----------------------------

st.subheader("Limitations")

st.markdown("""
The conclusions are based on the available dataset
and the visualizations presented in the EDA.

The analysis does not establish that a particular
vehicle characteristic directly causes a change
in selling price.

Additional information such as vehicle condition,
accident history, maintenance records, and optional
features could provide further context for used-car
valuation.
""")


st.success(
    "Exploratory Data Analysis completed. "
    "The visualizations provide a foundation for "
    "further investigation of used-car prices."
)