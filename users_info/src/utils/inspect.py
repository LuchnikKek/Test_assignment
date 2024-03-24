from sqlalchemy import inspect

from src.core.db import Base
import pprint


def inspect_model(model: type[Base]) -> None:
    """
    Выводит список всех колонок декларативной модели.
    Функция для дебага.

    :param model: Декларативная модель SQLAlchemy.
    """
    columns = list(inspect(model).columns)
    pprint.pprint(columns)
