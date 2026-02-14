# Weather Data Pipeline

This project implements an ETL (Extract, Transform, Load) pipeline to collect, process, and store weather data for the city of Paris using Apache Airflow.

## Features

- **Extraction**: Fetches weather data from the OpenWeatherMap API.
- **Transformation**: Cleans, converts, and formats the data (temperature, humidity, wind, etc.).
- **Loading**: Archives the data in CSV files and inserts it into a PostgreSQL database.

## Project Structure

```
my_weather_data_pipeline/
│
├── airflow/
│   ├── airflow.cfg
│   └── dags/
│       └── weather_dags.py
│
├── etl_functons/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── files_extracted/
│   └── extraction_YYYY-MM-DD_HHh.csv
│
├── requirements.txt
└── ...
```

## Installation

1. **Clone the repository**
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure Airflow**:
   - Initialize the Airflow database:
     ```bash
     airflow db init
     ```
   - Create a PostgreSQL connection in the Airflow UI (`postgres_conn`).
   - Set the Airflow variable `API_KEY` with your OpenWeatherMap API key.

## Usage

- Start the Airflow scheduler and webserver:
  ```bash
  airflow scheduler
  airflow webserver
  ```
- Enable the `first_weather_dag` DAG in the Airflow UI.
- Extractions run every hour at minute 30.
- Extracted files are saved in the `files_extracted/` folder.
- Data is inserted into the `weather_table` table in PostgreSQL.

## ETL Flow Example

1. **Extract**: Call the OpenWeatherMap API for Paris.
2. **Transform**: Convert temperatures to Celsius, format dates, etc.
3. **Load**:
   - Archive as CSV: `files_extracted/extraction_2026-01-08_13h.csv`
   - Insert into PostgreSQL database.

## Main Dependencies

- Apache Airflow
- pandas
- requests
- PostgreSQL

## Customization

- Change the target city in `extract.py` if needed.
- Adapt the PostgreSQL table structure as required.

## Author

Project by Arnel Fokou.
