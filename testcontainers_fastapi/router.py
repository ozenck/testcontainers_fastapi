from fastapi import APIRouter
from fastapi.responses import FileResponse
import tempfile

router = APIRouter()


def generate_sql_content() -> str:
    return """
    CREATE TABLE example_table (
        id INT PRIMARY KEY,
        name VARCHAR(100),
        age INT
    );

    INSERT INTO example_table (id, name, age) VALUES
    (1, 'Alice', 25),
    (2, 'Bob', 30),
    (3, 'Charlie', 35);
    """


def create_temp_sql_file(content: str, suffix: str = ".sql") -> str:
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp_file:
        temp_file.write(content.encode("utf-8"))
        return temp_file.name


@router.get("/export")
async def export_sql() -> FileResponse:
    file_path = create_temp_sql_file(generate_sql_content())
    return FileResponse(path=file_path, media_type="application/sql", filename="exported_data.sql")
