import streamlit as st

st.set_page_config(
    page_title="Cars EDA Dashboard",
    layout="wide"
)

st.title("Cars EDA Dashboard")

st.markdown("""
## Welcome to the Cars Data Analysis Dashboard

This dashboard presents an exploratory analysis of the car dataset.

Use the pages from the sidebar:

- **Introduction** – Dataset overview and project objective
- **EDA** – Interactive exploratory data analysis
- **Conclusion** – Key findings and insights
""")

st.info("Select a page from the sidebar to begin.")