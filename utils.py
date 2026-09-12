import pandas as pd


def load_data():

    df = pd.read_csv("Cars.csv")

    # Clean column names
    df.columns = (
        df.columns
        .astype(str)
        .str.strip()
        .str.replace(" ", "_", regex=False)
    )

    # Convert numeric columns
    for col in ["Year", "Price", "Kilometers_Driven",
                "Seats", "No._of_Doors"]:

        if col in df.columns:
            df[col] = pd.to_numeric(
                df[col],
                errors="coerce"
            )

    # Extract numeric values from text columns
    if "Mileage" in df.columns:
        df["Mileage_value"] = pd.to_numeric(
            df["Mileage"]
            .astype(str)
            .str.extract(r"([-+]?\d*\.?\d+)")[0],
            errors="coerce"
        )

    if "Engine" in df.columns:
        df["Engine_value"] = pd.to_numeric(
            df["Engine"]
            .astype(str)
            .str.extract(r"([-+]?\d*\.?\d+)")[0],
            errors="coerce"
        )

    if "Power" in df.columns:
        df["Power_value"] = pd.to_numeric(
            df["Power"]
            .astype(str)
            .str.extract(r"([-+]?\d*\.?\d+)")[0],
            errors="coerce"
        )

    # Company and model
    if "Name" in df.columns:

        df["Company_name"] = (
            df["Name"]
            .astype(str)
            .str.split()
            .str[0]
        )

        df["Model_name"] = (
            df["Name"]
            .astype(str)
            .str.split(n=1)
            .str[1]
            .fillna(df["Name"])
        )

    return df