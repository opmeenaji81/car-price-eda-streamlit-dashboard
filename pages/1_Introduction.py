import streamlit as st

st.set_page_config(
    page_title="Introduction",
    layout="wide"
)

st.title("Introduction")

st.markdown("""
## About the Project

This project focuses on the exploratory data analysis of a
car dataset.

The objective is to understand the characteristics of cars,
identify patterns in pricing, and explore how different factors
such as fuel type, transmission, location, company, and
kilometers driven are related to car prices.
""")

st.divider()

st.subheader("Project Objectives")

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    ### Data Understanding

    - Understand the structure of the dataset
    - Identify important variables
    - Check missing values
    - Examine data types
    - Detect possible inconsistencies
    """)

with col2:

    st.markdown("""
    ### Exploratory Analysis

    - Analyze car prices
    - Study fuel types
    - Compare transmissions
    - Analyze car companies
    - Explore locations
    - Study relationships between variables
    """)

st.divider()

st.subheader("Dataset Features")

st.markdown("""
Some important variables available in the dataset include:

| Feature | Description |
|---|---|
| `Name` | Name of the car |
| `Location` | Location where the car is listed |
| `Year` | Manufacturing year |
| `Kilometers_Driven` | Distance driven |
| `Fuel_Type` | Type of fuel |
| `Transmission` | Manual or automatic |
| `Owner` | Ownership information |
| `Mileage` | Mileage of the car |
| `Engine` | Engine capacity |
| `Power` | Engine power |
| `Seats` | Number of seats |
| `Price` | Selling price |
""")

st.divider()

st.info(
    "Move to the EDA page to explore the dataset interactively."
)