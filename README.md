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

## Installation instructions

## How to run the application

## An overview of the API endpoints
