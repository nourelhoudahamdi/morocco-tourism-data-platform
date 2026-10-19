# Morocco Tourism Data Platform

## 1. Project Overview

The Morocco Tourism Data Platform is a beginner-friendly Data Engineering project designed to collect, clean, store, and analyze tourism data related to Moroccan destinations.

The current version focuses on tourism overnight stays (*nuitées touristiques*) across 12 destinations in Morocco, covering the period from 2012 to 2020.

The goal is to transform raw tourism data into structured information that can help users understand tourism trends and compare destinations over time.

## 2. Project Objectives

* Ingest tourism data from CSV files.
* Clean and validate the data using Python.
* Store structured data in a PostgreSQL database.
* Analyze tourism trends across destinations.
* Compare tourism overnight stays between 2019 and 2020.
* Generate visualizations to communicate the results.
* Build a foundation for a more complete tourism analytics platform.

## 3. Data Pipeline Architecture

The current pipeline follows these steps:

```text
Raw CSV Data
     |
     v
Data Ingestion
     |
     v
Data Cleaning and Quality Checks
     |
     v
Processed CSV Data
     |
     v
PostgreSQL Database
     |
     v
Data Analysis
     |
     v
Visualization
```

## 4. Technologies Used

* **Python** — data processing and pipeline orchestration
* **Pandas** — data cleaning and analysis
* **PostgreSQL** — relational database storage
* **Matplotlib** — data visualization
* **Git** — version control

## 5. Project Structure

```text
morocco-tourism-data-platform/
├── data/
│   ├── raw/
│   │   └── tourism_nights_by_destination.csv
│   └── processed/
│       ├── tourism_nights_clean.csv
│       ├── tourism_analysis_results.csv
│       └── comparison_2019_2020.png
├── src/
│   ├── ingestion/
│   │   └── ingest_tourism_data.py
│   ├── database/
│   │   └── load_tourism_to_postgres.py
│   └── analytics/
│       ├── tourism_analysis.py
│       └── tourism_visualization.py
└── run_pipeline.py
```

## 6. Current Features

* CSV data ingestion
* Data cleaning and validation
* Missing-value and duplicate checks
* PostgreSQL loading
* Tourism data analysis
* Percentage variation calculation between 2019 and 2020
* Comparison chart generation
* Pipeline execution through a single Python command

## 7. Initial Findings

The current analysis shows that:

* Marrakech recorded the highest number of tourism overnight stays among the included destinations in 2019.
* Al Haouz experienced the largest percentage decrease in overnight stays between 2019 and 2020.
* All 12 destinations recorded a decrease over this period in the dataset.

These findings describe the available dataset and do not, by themselves, establish the causes of the changes.

## 8. How to Run the Project

### Prerequisites

* Python
* PostgreSQL
* A Python virtual environment with the required project packages installed

### Run the pipeline

Activate the project's virtual environment, open a terminal in the project root, and run:

```powershell
python .\run_pipeline.py
```

The pipeline executes data ingestion, PostgreSQL loading, analysis, and visualization.

### PostgreSQL password

The database loader expects the PostgreSQL password to be available through the `PGPASSWORD` environment variable.

In PowerShell, set it for the current terminal session with:

```powershell
$env:PGPASSWORD = Read-Host "Entrez le mot de passe PostgreSQL"
```

Enter the password locally when prompted. Do not publish your database password or commit it to Git.

## 9. Future Improvements

* Add more reliable tourism data sources.
* Automate data ingestion.
* Improve database design and SQL analytics.
* Add weather, events, and other relevant tourism indicators.
* Build an interactive dashboard.
* Add automated tests and pipeline logging.
* Publish project documentation and code on GitHub.

## 10. Project Status

**Current status:** Initial working pipeline.

The project currently processes tourism overnight-stay data for 12 Moroccan destinations from 2012 to 2020. Additional sources, automated ingestion, and interactive analytics are planned for future versions.
