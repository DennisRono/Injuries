# Injury Classification API

## Overview

The Injury Classification API is a comprehensive system designed to assist insurance companies in accurately classifying injuries, calculating severity, and managing claims. This API integrates international standards such as the International Classification of Diseases, 10th Revision (ICD-10), and the Abbreviated Injury Scale (AIS) to provide a robust framework for injury assessment and compensation calculation.

## Features

- **ICD-10 Integration**: Utilizes the International Classification of Diseases (ICD-10) for standardized injury coding.
- **AIS Implementation**: Incorporates the Abbreviated Injury Scale (AIS) for assessing injury severity.
- **Injury Severity Score (ISS) Calculation**: Automatically calculates the Injury Severity Score based on AIS codes.
- **Patient Management**: Allows creation and retrieval of patient records.
- **Claim Processing**: Facilitates the creation and management of insurance claims.
- **RESTful API**: Provides a clean and intuitive API for easy integration with existing systems.

## Technology Stack

- **Framework**: FastAPI
- **Database**: SQLite (easily adaptable to other SQL databases)
- **ORM**: SQLAlchemy
- **Data Validation**: Pydantic

## Project Structure

    injuries/
    ├── main.py
    ├── database.py
    ├── models/
    │   ├── __init__.py
    │   ├── base.py
    │   ├── icd10.py
    │   ├── ais.py
    │   ├── injury.py
    │   ├── claim.py
    │   └── patient.py
    ├── schemas/
    │   ├── __init__.py
    │   ├── icd10.py
    │   ├── ais.py
    │   ├── injury.py
    │   ├── claim.py
    │   └── patient.py
    ├── routers/
    │   ├── __init__.py
    │   ├── icd10.py
    │   ├── ais.py
    │   ├── injury.py
    │   ├── claim.py
    │   └── patient.py
    ├── services/
    │   ├── __init__.py
    │   └── injury_severity.py
    └── utils/
        ├── __init__.py
        └── time_utils.py

## Installation Instructions

1. **Clone the repository**
    ```sh
    git clone https://github.com/DennisRono/Injuries.git
    cd injury-classification-api
    ```
2. **Create a virtual environment and activate it**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. **Install dependencies**
    ```sh
    pip install -r requirements.txt
    ```
4. **Run database migrations**
    ```sh
    alembic upgrade head
    ```
5. **Start the FastAPI server**
    ```sh
    uvicorn main:app --reload
    ```
6. **Access API documentation**
    - Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for Swagger UI.
    - Open [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) for ReDoc UI.

## How to Run the Application

- Ensure you have Python 3.9+ installed.
- Follow the installation steps above.
- The API will be accessible at `http://127.0.0.1:8000/`.
- Use the provided API documentation to test endpoints.

## API Endpoints Overview

### ICD-10 Codes
| Method | Endpoint | Description |
|--------|---------|-------------|
| GET | `/icd10/` | Retrieve all ICD-10 codes |
| GET | `/icd10/{code}` | Retrieve details of a specific ICD-10 code |
| POST | `/icd10/` | Add a new ICD-10 code |
| DELETE | `/icd10/{code}` | Delete an ICD-10 code |

### AIS Codes
| Method | Endpoint | Description |
|--------|---------|-------------|
| GET | `/ais/` | Retrieve all AIS codes |
| GET | `/ais/{code}` | Retrieve details of a specific AIS code |
| POST | `/ais/` | Add a new AIS code |
| DELETE | `/ais/{code}` | Delete an AIS code |

### Injuries
| Method | Endpoint | Description |
|--------|---------|-------------|
| GET | `/injuries/` | Retrieve all injuries |
| GET | `/injuries/{id}` | Retrieve details of a specific injury |
| POST | `/injuries/` | Record a new injury |
| DELETE | `/injuries/{id}` | Delete an injury record |

### Patients
| Method | Endpoint | Description |
|--------|---------|-------------|
| GET | `/patients/` | Retrieve all patients |
| GET | `/patients/{id}` | Retrieve details of a specific patient |
| POST | `/patients/` | Add a new patient |
| DELETE | `/patients/{id}` | Delete a patient record |

### Claims
| Method | Endpoint | Description |
|--------|---------|-------------|
| GET | `/claims/` | Retrieve all claims |
| GET | `/claims/{id}` | Retrieve details of a specific claim |
| POST | `/claims/` | File a new claim |
| DELETE | `/claims/{id}` | Delete a claim record |

## License

This project is licensed under the **MIT License**.

