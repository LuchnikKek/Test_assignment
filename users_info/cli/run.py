import asyncio
from typing import Annotated

import typer
import os

from data_providers import get_data, get_mock_data
from config import logger

app = typer.Typer()


@app.command()
def migrate():
    """Применяет миграции."""
    os.system("alembic upgrade head")
    logger.info("Миграции применены.")


@app.command()
def create(
    from_net: Annotated[bool, typer.Option("--mock", "-m", help="Считать mock-данные, а не загружать по сети.")] = True
):
    """Заполняет базу данными."""
    if from_net:
        data = asyncio.run(get_data())
    else:
        data = asyncio.run(get_mock_data())

    logger.info("Загружено в базу.")


if __name__ == "__main__":
    app()
