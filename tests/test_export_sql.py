import mysql.connector.cursor
from fastapi.testclient import TestClient
import os
from testcontainers_fastapi.main import app
from typing import Callable

client = TestClient(app)


def download_sql_file(endpoint: str = "/export", filename: str = "exported_data.sql") -> str:
    response = client.get(endpoint)
    assert response.status_code == 200
    with open(filename, "wb") as f:
        f.write(response.content)
    return filename


def execute_sql_file(cursor: mysql.connector.cursor.MySQLCursor, sql_file_path: str) -> None:
    with open(sql_file_path, "r") as file:
        sql_commands = file.read().split(";")
        for command in sql_commands:
            if command.strip():
                cursor.execute(command)


def test_export_sql_to_mysql(get_db_connection: Callable[[], mysql.connector.connection.MySQLConnection]) -> None:
    sql_file_path = download_sql_file()

    connection = get_db_connection()
    try:
        cursor = connection.cursor()
        execute_sql_file(cursor, sql_file_path)
        connection.commit()

        cursor.execute("SELECT * FROM example_table;")
        rows = cursor.fetchall()
        expected_data = [(1, "Alice", 25), (2, "Bob", 30), (3, "Charlie", 35)]
        assert rows == expected_data

    finally:
        cursor.close()
        connection.close()
        os.remove(sql_file_path)
