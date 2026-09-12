import streamlit as st
import pandas as pd
import plotly.express as px

from utils import load_data


st.set_page_config(
    page_title="EDA",
    layout="wide"
)


# -----------------------------
# Load Data
# -----------------------------

df = load_data()


# -----------------------------
# Title
# -----------------------------

st.title("Exploratory Data Analysis")

st.caption(
    "Interactive exploration of the Cars dataset"
)


# -----------------------------
# Sidebar Filters
# -----------------------------

st.sidebar.header("Filters")


filtered = df.copy()


# Location
if "Location" in df.columns:

    locations = sorted(
        df["Location"]
        .dropna()
        .unique()
    )

    selected_locations = st.sidebar.multiselect(
        "Location",
        locations
    )

    if selected_locations:
        filtered = filtered[
            filtered["Location"].isin(selected_locations)
        ]


# Company
if "Company_name" in df.columns:

    companies = sorted(
        df["Company_name"]
        .dropna()
        .unique()
    )

    selected_companies = st.sidebar.multiselect(
        "Company",
        companies
    )

    if selected_companies:
        filtered = filtered[
            filtered["Company_name"].isin(selected_companies)
        ]


# Fuel
if "Fuel_Type" in df.columns:

    fuels = sorted(
        df["Fuel_Type"]
        .dropna()
        .unique()
    )

    selected_fuels = st.sidebar.multiselect(
        "Fuel Type",
        fuels
    )

    if selected_fuels:
        filtered = filtered[
            filtered["Fuel_Type"].isin(selected_fuels)
        ]


# Transmission
if "Transmission" in df.columns:

    transmissions = sorted(
        df["Transmission"]
        .dropna()
        .unique()
    )

    selected_transmission = st.sidebar.multiselect(
        "Transmission",
        transmissions
    )

    if selected_transmission:
        filtered = filtered[
            filtered["Transmission"].isin(selected_transmission)
        ]


# -----------------------------
# Year Filter
# -----------------------------

if "Year" in df.columns:

    min_year = int(df["Year"].min())
    max_year = int(df["Year"].max())

    year_range = st.sidebar.slider(
        "Year",
        min_year,
        max_year,
        (min_year, max_year)
    )

    filtered = filtered[
        filtered["Year"].between(
            year_range[0],
            year_range[1]
        )
    ]


# -----------------------------
# Price Filter
# -----------------------------

if "Price" in df.columns:

    min_price = float(df["Price"].min())
    max_price = float(df["Price"].max())

    price_range = st.sidebar.slider(
        "Price",
        min_price,
        max_price,
        (min_price, max_price)
    )

    filtered = filtered[
        filtered["Price"].between(
            price_range[0],
            price_range[1]
        )
    ]


# -----------------------------
# KPI Cards
# -----------------------------

st.subheader("Key Metrics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Cars",
        f"{len(filtered):,}"
    )

with col2:

    st.metric(
        "Average Price",
        f"{filtered['Price'].mean():.2f}"
    )

with col3:

    st.metric(
        "Avg. Kilometers",
        f"{filtered['Kilometers_Driven'].mean():,.0f}"
    )

with col4:

    st.metric(
        "Companies",
        f"{filtered['Company_name'].nunique():,}"
    )


st.divider()


# -----------------------------
# Tabs
# -----------------------------

overview, location, cars, price = st.tabs([
    "Overview",
    "Location",
    "Cars",
    "Price Analysis"
])


# =========================================================
# OVERVIEW
# =========================================================

with overview:

    st.header("Dataset Overview")

    col1, col2 = st.columns(2)

    # Fuel distribution
    with col1:

        fuel_data = (
            filtered["Fuel_Type"]
            .value_counts()
            .reset_index()
        )

        fuel_data.columns = [
            "Fuel_Type",
            "Count"
        ]

        fig = px.pie(
            fuel_data,
            names="Fuel_Type",
            values="Count",
            hole=0.4,
            title="Fuel Type Distribution"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # Transmission
    with col2:

        transmission_data = (
            filtered["Transmission"]
            .value_counts()
            .reset_index()
        )

        transmission_data.columns = [
            "Transmission",
            "Count"
        ]

        fig = px.bar(
            transmission_data,
            x="Transmission",
            y="Count",
            text="Count",
            title="Transmission Distribution"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # Cars by year

    yearly = (
        filtered
        .groupby("Year")
        .size()
        .reset_index(name="Cars")
    )

    fig = px.line(
        yearly,
        x="Year",
        y="Cars",
        markers=True,
        title="Number of Cars by Year"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =========================================================
# LOCATION
# =========================================================

with location:

    st.header("Location Analysis")

    location_data = (
        filtered["Location"]
        .value_counts()
        .head(15)
        .reset_index()
    )

    location_data.columns = [
        "Location",
        "Cars"
    ]

    fig = px.bar(
        location_data.sort_values("Cars"),
        x="Cars",
        y="Location",
        orientation="h",
        text="Cars",
        title="Top Locations by Number of Cars"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # Average price by location

    location_price = (
        filtered
        .groupby("Location")["Price"]
        .mean()
        .sort_values(ascending=False)
        .head(15)
        .reset_index()
    )

    fig = px.bar(
        location_price,
        x="Location",
        y="Price",
        title="Average Price by Location"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =========================================================
# CARS
# =========================================================

with cars:

    st.header("Car Analysis")

    col1, col2 = st.columns(2)


    # Companies

    with col1:

        company_data = (
            filtered["Company_name"]
            .value_counts()
            .head(15)
            .reset_index()
        )

        company_data.columns = [
            "Company",
            "Cars"
        ]

        fig = px.bar(
            company_data.sort_values("Cars"),
            x="Cars",
            y="Company",
            orientation="h",
            text="Cars",
            title="Top Car Companies"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # Owners

    with col2:

        owner_data = (
            filtered["Owner_Type"]
            .value_counts()
            .reset_index()
        )

        owner_data.columns = [
            "Owner_Type",
            "Cars"
        ]

        fig = px.bar(
            owner_data,
            x="Owner_Type",
            y="Cars",
            text="Cars",
            title="Cars by Owner Type"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        owner_data.columns = [
            "Owner",
            "Cars"
        ]

        fig = px.bar(
            owner_data,
            x="Owner",
            y="Cars",
            text="Cars",
            title="Cars by Owner Type"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # Numeric relationship

    st.subheader("Relationship Between Variables")

    numeric_columns = [
        "Year",
        "Kilometers_Driven",
        "Mileage_value",
        "Engine_value",
        "Power_value",
        "Price"
    ]

    numeric_columns = [
        col for col in numeric_columns
        if col in filtered.columns
    ]

    col1, col2 = st.columns(2)

    with col1:

        x_axis = st.selectbox(
            "X-axis",
            numeric_columns
        )

    with col2:

        y_axis = st.selectbox(
            "Y-axis",
            numeric_columns,
            index=min(1, len(numeric_columns) - 1)
        )

    fig = px.scatter(
        filtered,
        x=x_axis,
        y=y_axis,
        opacity=0.6,
        title=f"{y_axis} vs {x_axis}"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =========================================================
# PRICE
# =========================================================

with price:

    st.header("Price Analysis")


    col1, col2 = st.columns(2)


    # Price by fuel

    with col1:

        price_fuel = (
            filtered
            .groupby("Fuel_Type")["Price"]
            .mean()
            .reset_index()
        )

        fig = px.bar(
            price_fuel,
            x="Fuel_Type",
            y="Price",
            text_auto=".2f",
            title="Average Price by Fuel Type"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # Price by transmission

    with col2:

        price_transmission = (
            filtered
            .groupby("Transmission")["Price"]
            .mean()
            .reset_index()
        )

        fig = px.bar(
            price_transmission,
            x="Transmission",
            y="Price",
            text_auto=".2f",
            title="Average Price by Transmission"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # Price distribution

    fig = px.histogram(
        filtered,
        x="Price",
        nbins=40,
        title="Price Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# -----------------------------
# Data
# -----------------------------

st.divider()

st.subheader("Filtered Dataset")

st.dataframe(
    filtered,
    use_container_width=True,
    hide_index=True
)