# FastAPI MySQL Integration with Testcontainers

This project demonstrates how to use `FastAPI` in combination with `testcontainers` to perform integration testing on a MySQL database. By using Docker containers, the project can reliably spin up a fresh MySQL instance for each test session, ensuring isolated, consistent test environments.

## Features

- **FastAPI**: API endpoints with a simple SQL export functionality.
- **Testcontainers**: Automated container management for MySQL in integration tests.
- **MySQL Database**: Example of using a MySQL instance to store and retrieve data for tests.
- **Integration Testing**: Tests to verify SQL file export and execution functionality.

## Prerequisites

- **Python**: Make sure Python 3.8+ is installed, 3.13 provided in Dockerfile.
- **Docker**: Ensure Docker is installed and running to allow `testcontainers` to manage MySQL containers.

## Installation

1. **Clone the repository**:
   ```bash
   git clone git@github.com:ozenck/testcontainers_fastapi.git
   cd testcontainers_fastapi
   ```

2. **Install dependencies with Poetry**:
   ```bash
   poetry install
   ```

   if you have error because of python version, use latest version
   ```bash
   poetry env use "C:\Users\username\AppData\Local\Programs\Python\Python313\python.exe"
   ```
   and poetry install again.

3. **Run app**:
   ```bash
   poetry run uvicorn testcontainers_fastapi.main:app --reload
   ```
   or
   ```bash
   docker-compose up --build
   ```

4. **Run tests**:
   ```bash
   poetry run pytest
   ```


## Project Structure
- router.py: Contains the SQL export endpoint.
- conftest.py: Sets up pytest fixtures for MySQL containers and database connections.
- test_export_sql.py: Integration tests for the SQL export functionality.
- main.py: Main FastAPI app setup and endpoint inclusion.