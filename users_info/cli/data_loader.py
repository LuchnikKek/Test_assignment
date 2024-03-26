from typing import Any

import asyncpg
from uuid import uuid4
from config import DSN


def _columns_string(columns: list) -> str:
    """Возвращает из списка колонок строку.

    Пример:
    _columns_string(['col_1', 'col_2', 'col_3'])
    '(col_1, col_2, col_3)'
    """
    return "(" + ", ".join(columns) + ")"


def _template_string(columns: list) -> str:
    """Возвращает из списка колонок шаблон для подстановки значений.

    Пример:
    _template_string(['col_1', 'col_2', 'col_3'])
    '({col_1}, {col_2}, {col_3})'
    """
    return "(" + ", ".join("{%s}" % column for column in columns) + ")"


def _format_string(template: str, columns: list, row: dict) -> str:
    """Форматирует строку по шаблону и генерирует id. Все отсутствующие значения будут NULL."""
    row["id"] = uuid4()
    row = {k: "'%s'" % v for k, v in row.items()}
    [row.setdefault(val, "NULL") for val in columns]

    return template.format(**row)


def _prepare_insert_query(
    table: str,
    columns: list,
    values: list[dict],
) -> str:
    """Формирует bulk insert запрос."""
    columns_string = _columns_string(columns)  # '(col_1, col_2, col_3)'
    template = _template_string(columns)  # '({col_1}, {col_2}, {col_3})'
    values_string = ", ".join(_format_string(template, columns, row) for row in values)

    return """INSERT INTO {0} {1} VALUES {2}""".format(table, columns_string, values_string)


class PostgresWorker:
    def __init__(self):
        self.dsn = DSN

    async def execute_query(self, query: str) -> Any:
        conn: asyncpg.connection.Connection = await asyncpg.connect(dsn=self.dsn)

        try:
            return await conn.fetch(query)
        finally:
            await conn.close()

    async def is_table_empty(self, table: str) -> bool:
        """Возвращает True, если в таблице нет данных и False, если есть."""

        res = await self.execute_query("SELECT * FROM {} LIMIT 1;".format(table))
        return len(res) == 0

    async def columns(self, table: str) -> list:
        """Возвращает список колонок по названию таблицы"""
        query = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'%s'" % table
        columns = await self.execute_query(query)
        return [col.get("column_name") for col in columns]

    async def insert_data(self, table: str, data: list[dict]):
        """Вставляет данные в таблицу. Использует всего один INSERT."""
        columns = await self.columns(table)
        columns.remove("created_at")
        columns.remove("updated_at")

        query = _prepare_insert_query(table, columns, data)
        await self.execute_query(query)
