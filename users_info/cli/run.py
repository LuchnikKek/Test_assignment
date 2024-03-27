import asyncio
import os
from typing import Annotated

import typer
from config import DEBUG, logger
from data_loader import PostgresWorker
from data_providers import get_data, get_mock_data

app = typer.Typer()


@app.command()
def migrate():
    """Применяет миграции."""
    if DEBUG:
        os.system("env")
    os.system("alembic upgrade head")
    logger.info("Миграции применены.")


@app.command()
def create(
    mocked: Annotated[bool, typer.Option("--mock", "-m", help="Считать mock-данные, а не загружать по сети.")] = False
):
    """Заполняет базу данными."""
    pw = PostgresWorker()

    if not asyncio.run(pw.is_table_empty("users_table")):
        logger.error("В базе уже есть данные. Insert пропущен.")
        raise typer.Exit()

    data = asyncio.run(get_mock_data() if mocked else get_data())
    asyncio.run(pw.insert_data("users_table", data))

    logger.info("Данные загружены в базу.")


if __name__ == "__main__":
    app()
