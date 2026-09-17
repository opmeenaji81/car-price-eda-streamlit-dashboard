
import streamlit as st

st.set_page_config(
    page_title="Conclusion",
    layout="wide"
)

st.title("Conclusion")

st.markdown("""
The exploratory data analysis helped identify patterns
in used-car prices and examine the relationships between
price and different vehicle characteristics.

The following findings include numerical results reported
in the project analysis document.
""")

st.divider()

st.subheader("Key Numerical Findings")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        label="Correlation: Kilometers Driven vs Price",
        value="-0.63"
    )

    st.markdown("""
    The project document reports a negative correlation
    between kilometers driven and car price.

    This indicates that cars with higher kilometers driven
    tend to be associated with lower prices in the analyzed
    data.
    """)

with col2:
    st.metric(
        label="Correlation: Engine Value vs Price",
        value="0.66"
    )

    st.markdown("""
    The project document reports a positive relationship
    between engine value and car price.

    This indicates that cars with larger engine values
    tend to be associated with higher prices in the
    analyzed data.
    """)

st.divider()

st.subheader("Analysis Scale and Automation")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        label="Automobile Records",
        value="5,900+"
    )

    st.markdown("""
    The project document describes an analysis involving
    more than 5,900 automobile records and over 15
    attributes.
    """)

with col2:
    st.metric(
        label="Reported Reduction in Manual Analysis Time",
        value="Around 70%"
    )

    st.markdown("""
    The project document reports that automated
    visualizations reduced manual analysis time by
    approximately 70% when evaluating the dataset.
    """)

st.divider()

st.subheader("Car Characteristics and Pricing")

st.markdown("""
The analysis document identifies several vehicle
characteristics that may be associated with used-car prices:

- **Manufacturing year:** Older cars may experience
  depreciation and changes in demand.
- **Kilometers driven:** The reported correlation of
  -0.63 indicates a negative relationship with price.
- **Engine value:** The reported correlation of 0.66
  indicates a positive relationship with price.
- **Transmission:** The document notes that automatic
  cars sell at higher prices.
- **Fuel type:** The document discusses diesel-car demand
  in relation to increasing petrol prices.
- **Brand and model:** Maruti, Hyundai, and Honda are
  identified in the document as popular, lower-budget
  brands in the used-car market.
""")

st.divider()

st.subheader("Location Insights")

st.markdown("""
The project document identifies Mumbai and Hyderabad
as potentially popular used-car markets.

However, it also notes that this observation needs to
be verified using more data from other demographic
regions.

Further analysis could compare locations and investigate
whether separate groups of cars or locations should be
studied independently.
""")

st.divider()

st.subheader("Additional Factors to Consider")

st.markdown("""
The document also identifies factors that are not fully
represented by the numerical relationships discussed above:

- Vehicle wear and tear
- Accident history
- Air conditioning, moonroof, and airbags
- Maintenance and servicing requirements
- Customer test-drive and maintenance-package schemes
""")

st.divider()

st.subheader("Overall Conclusion")

st.markdown("""
The analysis document reports that kilometers driven
has a negative correlation with price (-0.63), while
engine value has a positive correlation with price (0.66).

These findings indicate that vehicle usage and engine
characteristics are associated with used-car prices
in the analyzed dataset.

Other characteristics, including manufacturing year,
fuel type, transmission, brand, and location, are also
discussed as relevant areas of analysis.

The results provide a foundation for further
investigation. Additional data on vehicle condition,
accident history, features, and geographic markets
could help develop a more comprehensive understanding
of used-car valuation.
""")

st.caption(
    "Note: Numerical findings shown here are reported "
    "in the project document. Correlation indicates "
    "association and does not establish causation."
)

st.success(
    "Exploratory Data Analysis completed. "
    "The findings can support further statistical "
    "analysis and future car price prediction work."
)