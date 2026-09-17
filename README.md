# Car Price EDA & Interactive Dashboard

An interactive web application for exploring car data, analyzing price patterns, and visualizing relationships between vehicle characteristics using Python and Streamlit.

## Live Demo

<a href="https://edaofcars.streamlit.app/" target="_blank" rel="noopener noreferrer">
  Open the Car EDA Dashboard
</a>

## Features

* Interactive filters for location, company, fuel type, transmission, year, and price.
* Key metrics including total cars, average price, average kilometers driven, and number of companies.
* Exploratory visualizations for car characteristics, locations, and prices.
* Filtered dataset viewing.

## Technologies Used

* Python
* Pandas
* NumPy
* Plotly
* Streamlit

## Project Structure

```text
car-price-eda-streamlit-dashboard/
├── app.py
├── utils.py
├── Cars.csv
├── requirements.txt
└── pages/
    ├── 1_Introduction.py
    ├── 2_EDA.py
    └── 3_Conclusion.py
```

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/opmeenaji81/car-price-eda-streamlit-dashboard.git
```

### 2. Navigate to the project folder

```bash
cd car-price-eda-streamlit-dashboard
```

### 3. (Optional) Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Windows PowerShell**

```powershell
.venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python -m streamlit run app.py
```

The application will open in your browser, usually at `http://localhost:8501`.

## Customization

You can modify this project for your own analysis:

* **`app.py`** — Edit the homepage.
* **`utils.py`** — Modify data loading and preprocessing.
* **`pages/1_Introduction.py`** — Update the project introduction.
* **`pages/2_EDA.py`** — Add or modify filters, metrics, and charts.
* **`pages/3_Conclusion.py`** — Update the conclusions and findings.
* **`Cars.csv`** — Replace the dataset, ensuring the column names and structure are compatible with the code.

After making changes, save your files and rerun the Streamlit app. To publish your changes, commit and push them to your GitHub repository.

## Contributions

Suggestions and improvements are welcome. Feel free to fork the repository, make changes, and submit a pull request.

## Author

**Omprakash**
