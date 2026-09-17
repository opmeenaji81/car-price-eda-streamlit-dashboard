
import streamlit as st

st.set_page_config(
    page_title="Introduction",
    layout="wide"
)

st.title("Introduction")

st.markdown("""
This analysis explores the factors associated with the
selling prices of used cars in India.

The dataset contains information about car manufacturers,
models, manufacturing years, kilometers driven, fuel types,
transmission, engine capacity, power, and other attributes.

The analysis focuses on understanding the dataset,
identifying patterns, and examining how different car
characteristics are related to selling prices.
""")

st.divider()

st.subheader("Objectives of the Analysis")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### Data Understanding

    - Understand the structure of the dataset
    - Identify important variables
    - Examine data types
    - Identify missing values
    - Check possible data inconsistencies
    """)

with col2:
    st.markdown("""
    ### Exploratory Data Analysis

    - Analyze the distribution of car prices
    - Compare prices across fuel types
    - Examine manual and automatic transmissions
    - Explore car manufacturers and models
    - Analyze differences across locations
    - Investigate relationships between variables
    """)

st.divider()

st.subheader("Dataset Features")

st.markdown("""
The dataset includes the following important attributes:
""")

st.markdown("""
| Feature | Description |
|---|---|
| `Name` | Car brand and model name |
| `Location` | City where the car is listed |
| `Year` | Manufacturing year |
| `Kilometers_Driven` | Distance driven by the car |
| `Fuel_Type` | Type of fuel used |
| `Transmission` | Manual or automatic transmission |
| `Owner_Type` | Ownership information |
| `Mileage` | Mileage of the car |
| `Engine` | Engine capacity |
| `Power` | Engine power |
| `Seats` | Number of seats |
| `Price` | Selling price of the used car |
""")

st.divider()

st.subheader("Questions Investigated")

st.markdown("""
- How do car characteristics relate to selling price?
- Does the car's brand or model have a relationship with price?
- How does transmission type relate to price?
- Does the selling location show differences in price?
- How are manufacturing year and kilometers driven
  associated with price?
- How do mileage, engine capacity, and power relate to price?
- How do fuel type and number of seats relate to price?
""")

st.divider()

st.info(
    "Proceed to the EDA page to explore the data "
    "and examine these relationships through visualizations."
)