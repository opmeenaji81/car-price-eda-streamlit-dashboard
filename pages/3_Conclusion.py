import streamlit as st

st.set_page_config(
    page_title="Conclusion",
    layout="wide"
)

st.title("Conclusion")

st.markdown("""
## Key Findings

The exploratory data analysis helped us understand the major
patterns present in the car dataset.
""")

st.divider()

col1, col2 = st.columns(2)

with col1:

    st.subheader("Car Characteristics")

    st.markdown("""
    - The dataset contains cars from multiple manufacturers.
    - Different fuel types are represented in the dataset.
    - Both manual and automatic transmission cars are present.
    - Cars vary significantly in age, mileage, engine capacity,
      and power.
    """)


with col2:

    st.subheader("Price Insights")

    st.markdown("""
    - Car prices vary considerably across different models.
    - Fuel type has an observable relationship with price.
    - Transmission type can also influence average price.
    - Newer cars generally tend to have higher prices.
    """)


st.divider()

st.subheader("Location Insights")

st.markdown("""
The number of cars listed varies considerably across locations.
Some locations have a much larger number of listings than others,
which can influence the overall distribution of prices and car
characteristics.
""")


st.divider()

st.subheader("Overall Conclusion")

st.markdown("""
The EDA shows that car price is influenced by several factors
rather than a single variable.

Important factors include:

- **Car age**
- **Kilometers driven**
- **Fuel type**
- **Transmission**
- **Engine**
- **Power**
- **Car manufacturer**
- **Location**

The analysis provides a useful understanding of the dataset and
can serve as a foundation for further analysis or a machine
learning model for car price prediction.
""")


st.divider()

st.success(
    "EDA completed — the dataset is ready for deeper statistical "
    "analysis or predictive modeling."
)