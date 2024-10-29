import pytest
from testcontainers.mysql import MySqlContainer
import mysql.connector
from mysql.connector.connection import MySQLConnection
from typing import Generator, TYPE_CHECKING, Callable, cast

if TYPE_CHECKING:
    from mysql.connector.connection import MySQLConnection


@pytest.fixture(scope="session")
def mysql_container() -> Generator[MySqlContainer, None, None]:
    with MySqlContainer("mysql:8.0") as mysql:
        yield mysql


@pytest.fixture(scope="session")
def get_db_connection(mysql_container: MySqlContainer) -> Callable[[], MySQLConnection]:
    def _connect() -> MySQLConnection:
        connection = mysql.connector.connect(
            host=mysql_container.get_container_host_ip(),
            port=mysql_container.get_exposed_port(3306),
            user=mysql_container.username,
            password=mysql_container.password,
            database=mysql_container.dbname,
        )
        return cast(MySQLConnection, connection)

    return _connect
