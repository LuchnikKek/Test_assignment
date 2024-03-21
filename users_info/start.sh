#!/bin/bash

set -eo pipefail
shopt -s nullglob

#alembic upgrade head
#exec скрипт для создания пользователей

exec uvicorn src.main:app --host 0.0.0.0 --port "$API_PORT" --reload
